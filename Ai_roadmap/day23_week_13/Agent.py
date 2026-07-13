import datetime
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

def check_string(s):
    safe = ["+", "-", "*", "/", "(", ")"," ",".","%"]
    for i in s:
        if i.isdigit() or i in safe:
            pass 
        else:
            return False
    return True
@tool
def calculator(expression:str)->str:
    """ it takes a string expression as an input and performs additon,substraction , multiplitcation , division , modulo and returns output or error message if any"""
    if check_string(expression):
        try:
            return eval(expression)
        except:
            return "Invalid Expression!"
    else:
        return "Error: Unsafe expression! "
@tool
def get_current_time() -> str:
    """It doesnt take any input , but it returns the current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
agent = create_agent(
    model="groq:llama-3.3-70b-versatile",
    tools=[calculator,get_current_time]
)
for chunk in agent.stream(
    {"messages":[{'role':'user','content':"get the current time and i need u to perform multiplication between hour and minute, and then add the seconds to it"}]},
    stream_mode= "values"
):
    print(chunk)
    print("-------")
    