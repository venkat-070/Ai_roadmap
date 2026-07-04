from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0.2
)

response = llm.invoke("What is an habit?")
print(response.content)