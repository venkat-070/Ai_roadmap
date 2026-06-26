import os 
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("GROQ")
client = Groq(api_key=api_key)
zero_shot = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [{
        "role":"user","content":"The delivery was late by 3 days, but the product quality exceeded my expectations."
    }]
)
print("zero_shot: \n",zero_shot.choices[0].message.content)
Few_shot = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [{
        "role":"user","content": '''
The delivery was late by 3 days, but the product quality exceeded my expectations.

Examples:
"The product has extraordinary durability." -> positive
"The product has some fluctuations during heavy usage but overall is good." -> neutral
"The product cannot process even low-grade tasks correctly." -> negative

Return ONLY valid JSON in exactly this format:

{
    "sentiment": "positive",
    "reason": "one sentence",
    "confidence": "high"
}
'''
    }]
)
raw = Few_shot.choices[0].message.content.strip()
raw = raw.replace("```json","").replace("```","")
data = json.loads(raw)
print("Few_shot: ",data)
Chain_of_thought = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [{
        "role":"user","content":'''The delivery was late by 3 days, 
        but the product quality exceeded my expectations.
        Produce the output in step by step manner stating the reason
        '''
    }]
)
print(Chain_of_thought.choices[0].message.content)