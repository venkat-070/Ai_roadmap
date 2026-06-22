import os
from dotenv import load_dotenv
from google import genai
import ssl
import certifi

# Fix SSL certificates
os.environ["SSL_CERT_FILE"] = certifi.where()

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

# Make your first API call
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what an LLM is in 3 sentences."
)

# Extract and print the text
print(response.text)