from models import model
from tools import calculate_right_refund, issue_refund_ticket, get_user_purchase_history
from dotenv import load_dotenv
from langchain.agents import create_agent
from prompts import agent_system_prompt
from objects import Answer
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage

load_dotenv()

agent = create_agent(
    model=model,
    system_prompt=agent_system_prompt,
    tools=[get_user_purchase_history,calculate_right_refund,issue_refund_ticket],
    response_format=Answer,
    checkpointer=InMemorySaver()
)

config = {"configurable": {"thread_id": "1"}}

question = HumanMessage(content="I would like to request a refund")
conversation = True


# conversation
while conversation:

    # invoking our agent
    response = agent.invoke({"messages": question},config=config)
    # collecting the structured response
    structured_response = response["structured_response"]

    print(structured_response.answer)

    user_input = input("reply: \n")
    question = HumanMessage(content=user_input)

    conversation = structured_response.conversation

print("the job is done!")

