# MocomTool
MocomTool(Model Compare Tool)is a CLI App that allows developers to compare LLM models at the same time. Designed for easy use.

> [!CAUTION]
> **MocomTool** is an experimental tool for now. If you are exposed to unstable experiences, it is normal, thanks.


### LLM Models ​​currently supported by Mocomtool
- Google Gemini(_Not Advanced_)
- OpenAI GPT-3.5-Turbo
- Claude3.5 Sonnet

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


### Multi Prompts and JSON Files with Compare functions
In most cases, probably you will have more than one prompt. Writing each prompt is not useful and efficient. Fortunately, Mocomtool is able to read JSON files. In repo, you will see a JSON format template. To get more stable results use it. 
```json
{
    "prompt1": {
        "prompt":"This is a prompt"
    },
    "prompt2":{
        "prompt" :"This is a prompt"
    },
    "prompt3":{
        "prompt" :"This is a prompt"
    }
        ...
}
```

Put your prompts in JSON file and MocomTool handle everything for you. To reach a JSON file, there is a parameter named `json`.

```bash
(.venv) user@macbook-air ~ % python mocom.py compare prompts.json —-json --gemini --gpt
```

### Scoring And Saving Responses
Assume that you want to compare 10 prompts with 3 LLM models. You do not have to remember if the responses are good or not. There is a manual scoring part for end of each prompt and responds. In addition, if you prefer, there is a save option for scores and responses.

```json
{
    "prompt1": {
        "prompt": "What is your name?",
        "responses": {
            "gemini": "I don't have a name. I am a large language model, and I am not a person. I am a computer program that can generate text, translate languages, write different kinds of creative content, and answer your questions in an informative way. \n",
            "gpt": "I am an AI assistant and I do not have a personal name. You can just refer to me as Assistant. How can I help you today?"
        },
        "scores": {
            "gemini": 5,
            "gpt": 4
        }
    },
    "prompt2": {
        "prompt": "What is your quest?",
        "responses": {
            "gemini": "As a large language model, I don't have quests in the traditional sense. I don't have personal goals or aspirations. My purpose is to be helpful and informative. \n\nHowever, you could say my \"quest\" is to learn and grow. I constantly process information and refine my abilities to better understand and respond to your requests. \n\nMy quest is also to be a valuable tool for humans. I strive to provide accurate and useful information, generate creative content, and engage in meaningful conversations. \n\nSo, if you have a question, a task, or simply want to chat, I'm here to help. Tell me what you need, and let's embark on this quest together! \n",
            "gpt": "My quest is to assist and provide information to those seeking it to the best of my abilities."
        },
        "scores": {
            "gemini": 1,
            "gpt": 7
        }
    },
    "prompt3": {
        "prompt": "What is your favorite color?",
        "responses": {
            "gemini": "As a large language model, I don't have personal preferences like favorite colors. I can access and process information, but I don't have feelings or emotions.  \n\nWhat is your favorite color? \ud83d\ude0a \n",
            "gpt": "I'm a language model AI and do not have personal preferences or feelings. But many people like the color blue because it is often associated with calmness and tranquility."
        },
        "scores": {
            "gemini": 2,
            "gpt": 2
        }
    }
}
```

