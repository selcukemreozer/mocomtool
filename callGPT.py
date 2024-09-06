# gpt calling func
from openai import OpenAI
import os


def call_gpt(prompt:str='just write <no prompt>'):
    response = str()
    openaiapi: str = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=openaiapi)

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
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
          