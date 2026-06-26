import os 
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GROQ")
client = Groq(api_key=api_key)
response = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [{"role":"user","content":'''A freelancer charges ₹500 per hour.
    He worked 3 hours on Monday, 4.5 hours on Tuesday, and 2 hours on Wednesday.
    He gives a 10 percent discount if the total bill exceeds ₹2000.
    What is the final amount the client pays?'''}]
)
print("Direct: ",response.choices[0].message.content)
response2 = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [{"role":"user","content":'''A freelancer charges ₹500 per hour.
    He worked 3 hours on Monday, 4.5 hours on Tuesday, and 2 hours on Wednesday.
    He gives a 10 percent discount if the total bill exceeds ₹2000.
    What is the final amount the client pays?, step by setp '''}]
)
print("Chain of thought:",response2.choices[0].message.content)