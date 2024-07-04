# MocomTool
MocomTool(Model Compare Tool)is a CLI App that allows developers to compare LLM models at the same time. Designed for easy use.

> [!CAUTION]
> **MocomTool** is an experimental tool for now. If you are exposed to unstable experiences, it is normal, thanks.


### LLM Models ​​currently supported by Mocomtool
- Google Gemini(_Not Advanced_)
- OpenAI GPT-3.5-Turbo
- Claude3.5 Sonnet(_soon_)

## What Exactly MocomTool is
MocomTool does not enable users to reach LLM models without `API KEYs` provided by services. To use MocomTool, you need a `.env` file that includes API keys.
You can find a template for the `.env` file named `env_template` in this repo. Check it. The tool is a helper for developers in choosing the best LLM model in their case.

> [!TIP]
> Before starting, you might prefer to install requirements for an easy installation.
```bash
(.venv) user@macbook-air ~ % pip install -r requirements.txt
```
## Help
#### Function [introduce]
MocomTool includes a guide. When you are stuck while using MocomTool call the `[introduce]` function, to see functions and parameters, which you can use.
```bash
(.venv) user@macbook-air ~ % python mocom.py introduce
```
## Giving Basic Prompts and Choosing Models for Comparing
After installing MocomTool from this repo, you will run `mocom.py` in `Terminal`. MocomTool was designed as a CLI App. So you can use it from the Terminal easily.

#### Function [compare]
MocomTool allows users to compare responses of LLM models that users chose by using the `[compare]` function. To use it, call the function, write your prompt `’my prompt in backticks’`, and choose the models that you want to compare. A distinct example below:

```bash
(.venv) user@macbook-air ~ % python mocom.py compare ’introduce yourself’ --gemini --gpt
```

Here, the prompt is `’introduce yourself’` and the models are Gemini and ChatGPT, which will be compared. The output will be:

```bash

prompt: introduce yourself


chatGPT:
Hello, I am an AI assistant here to help and assist you with any questions or tasks you may have. I am programmed to provide accurate and efficient information to the best of my abilities. How may I assist you today?

Gemini:
Hello! I am a large language model, trained by Google. 

Here are some things you should know about me:

* **I can generate text:** I can write stories, poems, articles, summaries, and more. 
* **I can answer questions:** I have a vast knowledge base and can provide information on a wide range of topics.
* **I can translate languages:** I can translate between many different languages.
* **I am still under development:** I am constantly learning and improving.

I am here to assist you with your questions and tasks.  What can I help you with today? 

```
> [!NOTE]
> Even though, in models versions cannot be chosen on Terminal(exp. between GPT-4 or GPT-3.5-turbo, etc.), you can change your model versions manually. This feature will be added in the future.




