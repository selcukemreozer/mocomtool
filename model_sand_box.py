"""
    _summary_ creates a stream of messages between the user and the model. 
    OpenAI's GPT-3.5-turbo model is used to generate responses to the user's messages. The model is initialized with the API key and the stream is created with the model and the messages. The stream is iterated over and the model's responses are printed to the console.
    my personal api is being used to access the model.
"""

"""
from openai import OpenAI
import os
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "sen kaba bir kisisin ve cok kisa cevaplar veriyorsun. Argolu bir dilin var"},
        {"role": "user", "content": "kardesim odev yapmiyor cozum ne"},
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
"""

##############################################################################################################
"""
# claude api key: secret_

import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="api_key",
)
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)
"""
##############################################################################################################

# gemini api key: secret_

"""
import google.generativeai as genai
import PIL.Image
import os # connect with os library

googleapi: str = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=googleapi) # connect with the api key
#img = PIL.Image.open('path/to/image.png')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["hello?"])
print(response.text)
"""
##############################################################################################################
"""
import transformers
import torch

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

pipeline = transformers.pipeline(
  "text-generation",
  model="meta-llama/Meta-Llama-3-8B-Instruct",
  model_kwargs={"torch_dtype": torch.bfloat16},
  device="cuda",
)
"""