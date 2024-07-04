# gpt calling func
from openai import OpenAI
import os

response = str()
def call_gpt(prompt:str='just write <no prompt>'):
    openaiapi: str = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=openaiapi)

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            #{"role": "system", "content": ""},
            {"role": "user", "content": prompt},
        ],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

          
def call_gpt_test(prompt:str='just write <no prompt>'):
    openaiapi: str = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=openaiapi)

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            #{"role": "system", "content": ""},
            {"role": "user", "content": prompt},
        ],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response +=chunk.choices[0].delta.content
    
    return response