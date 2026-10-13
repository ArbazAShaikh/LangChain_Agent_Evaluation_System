from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
model = init_chat_model(model="gpt-6-luna")


#responce = model.invoke("tell me about the color blue in 3 sentences")
#print(responce.content)