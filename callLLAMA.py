import ollama
from groq import Groq
import os

def call_ollama(prompt:str='just write <no prompt>'):
    response = str()
    response = ollama.chat(model='llama3.1:8b', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response['message']['content']

def call_groq(prompt:str='just write <no prompt>'):
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
        model="llama-3.1-70b-versatile",
    )

    return chat_completion.choices[0].message.content

response = call_groq(prompt='What is the meaning of life?')
print(response)