import ollama
from groq import Groq
import os
from .models import OLLAMA_MODEL_NAME, GROQ_MODEL_NAME

def call_ollama(prompt:str='just write <no prompt>') -> list:
    response = str()
    response = ollama.chat(model=OLLAMA_MODEL_NAME, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return [response['message']['content'], OLLAMA_MODEL_NAME]

def call_groq(prompt:str='just write <no prompt>') -> str:
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=GROQ_MODEL_NAME,
    )

    return [chat_completion.choices[0].message.content, GROQ_MODEL_NAME]
