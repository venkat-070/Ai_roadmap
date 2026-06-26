import os 
from google import genai
from dotenv import load_dotenv
import json
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY2")
client = genai.Client(api_key=api_key)

reviews = ["The product broke after one day.",
"It's okay, nothing special.",
"Best purchase I've made this year!"]

for i in reviews:
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = f'''
        Analyse the review and get the output as the exact structre:
        review: {i}
        {{
  "sentiment": "positive/negative/neutral",
  "reason": "one sentence",
  "confidence": "high/medium/low"
}}'''
    )
    #print(response.text)
    raw = response.text.strip()
    raw = raw.replace("```json","").replace("```","").strip()
    data = json.loads(raw)
    print(data)