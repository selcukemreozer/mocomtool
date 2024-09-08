# gemini calling func
import google.generativeai as genai
from .models import GEMINI_MODEL_NAME
import os

def call_gemini(prompt:str='just write <no prompt>'):
    googleapi: str = os.environ.get("GOOGLE_API_KEY")  
    
    genai.configure(api_key=googleapi) # connect with the api key
    
    model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)
    response = model.generate_content([prompt])
    return [response.text, GEMINI_MODEL_NAME]
    