import os 
from google import genai 
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
review = ["The product broke after one day.","It's okay, nothing special.","Best purchase I've made this year!"]
for i in review:
    
    reponse1 = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = f"Classify customer reviews as: positive, negative, or neutral\n Review:{i}"
    )

    print(reponse1.text)
    reponse2 = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = f'''Classify customer reviews as: positive, negative, or neutral
            example: 
            this is best product - positive 
            this is good but need impovememt - nuetral 
            this is a bad product - negative
            Review:
            {i}
            '''
    )
    print(reponse2.text)