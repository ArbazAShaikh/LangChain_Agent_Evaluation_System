from langchain.tools import tool
from data import users_data
from dotenv import load_dotenv
import logging
from objects import PurchaseItem

load_dotenv()

# logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

@tool
def get_user_purchase_history(user:str) -> dict:
    """This tool takes the user username and return a dict of what the user has purchased"""
    logging.info(f"using get_user_purchase_history tool to get user's {user} purchase history")
    if users_data.get(user):
        return users_data[user]
    return {"status": "there was no username found"}



@tool
def calculate_right_refund(user:str, items:list[PurchaseItem]) -> str:
    """This tool takes a list of the items to be returned and the username and will return how much the refund is worth"""
    logging.info(f"using calculate_right_refund tool to get user's {user} refund")
    if users_data[user]:
            
            total_refund = 0

            for item in items:
                if users_data[user][item.name]:
                    total_refund += users_data[user][item.name]["price"]

            return f"the value of refund is: {total_refund}"
    return {"status": "there was no username found"}

@tool 
def issue_refund_ticket(refund_amount:int) -> str:
    """this tool will send a ticket to the teams to return a refund"""
    logging.info(f"using issue_refund_ticket tool")
    return f"a refund ticket has been issued successfully witht the amount of {refund_amount}"

#print(get_user_purchase_history.invoke("user123"))
"""
result = calculate_right_refund.invoke({
    "user": "user123",
    "items": ["book", "pen"]
})

print(result)
"""
#print(issue_refund_ticket.invoke("20"))