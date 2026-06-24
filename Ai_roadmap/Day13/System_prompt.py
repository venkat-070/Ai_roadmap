import os 
from google import genai
from google.genai import types 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "Tell me about dogs.",
    config = types.GenerateContentConfig(
        system_instruction = "You are a veterinary doctor. Always respond in exactly 3 bullet points. Be professional and concise.",
        temperature = 0.0
    )
)

print(response.text)