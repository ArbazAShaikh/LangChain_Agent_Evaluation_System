from dotenv import load_dotenv
import streamlit as st
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from models import model
from objects import Answer
from prompts import agent_system_prompt
from tools import (
    calculate_right_refund,
    get_user_purchase_history,
    issue_refund_ticket,
)


load_dotenv()

INITIAL_QUESTION = "I would like to request a refund"
THREAD_ID = "1"


def build_agent():
    return create_agent(
        model=model,
        system_prompt=agent_system_prompt,
        tools=[
            get_user_purchase_history,
            calculate_right_refund,
            issue_refund_ticket,
        ],
        response_format=Answer,
        checkpointer=InMemorySaver(),
    )


def invoke_agent(question: str) -> Answer:
    config = {"configurable": {"thread_id": THREAD_ID}}
    response = st.session_state.agent.invoke(
        {"messages": HumanMessage(content=question)},
        config=config,
    )
    return response["structured_response"]


def reset_conversation():
    st.session_state.agent = build_agent()
    st.session_state.messages = []
    st.session_state.conversation = True
    st.session_state.started = False


def start_conversation():
    st.session_state.messages.append({"role": "user", "content": INITIAL_QUESTION})
    structured_response = invoke_agent(INITIAL_QUESTION)
    st.session_state.messages.append(
        {"role": "assistant", "content": structured_response.answer}
    )
    st.session_state.conversation = structured_response.conversation
    st.session_state.started = True


st.set_page_config(page_title="Refund Agent", page_icon=":moneybag:")
st.title("Refund Agent")

if "agent" not in st.session_state:
    reset_conversation()

with st.sidebar:
    st.subheader("Session")
    st.caption(f"Thread ID: {THREAD_ID}")
    if st.button("Reset conversation", use_container_width=True):
        reset_conversation()
        st.rerun()

if not st.session_state.started:
    with st.spinner("Starting refund conversation..."):
        start_conversation()
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.conversation:
    user_input = st.chat_input("Reply")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                structured_response = invoke_agent(user_input)
                st.write(structured_response.answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": structured_response.answer}
        )
        st.session_state.conversation = structured_response.conversation
        st.rerun()
else:
    st.success("The job is done!")
