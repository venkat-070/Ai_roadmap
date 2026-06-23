import os 
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

response1 = client.models.generate_content(
model = "gemini-2.5-flash",
contents = "Give me a creative name for a coffee shop. Just the name, nothing else.",
config = types.GenerateContentConfig(temperature = 0.0)
)

response2 = client.models.generate_content(
model = "gemini-2.5-flash",
contents = "Give me a creative name for a coffee shop. Just the name, nothing else.",
config = types.GenerateContentConfig(temperature = 2.0)
)
print(response1.text)
print(response2.text)

