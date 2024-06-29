# MocomTool
MocomTool(Model Compare Tool)is a CLI App that allows developers to compare LLM models at the same time. Designed for easy use.

> [!CAUTION]
> **MocomTool** is a experimental tool for now. If you are exposed to unstable experience, it is normal, thanks.


### LLM Models ​​currently supported by Mocomtool
- Google Gemini(_Not Advanced_)
- OpenAI GPT-3.5-Turbo
- Claude3.5 Sonnet(_soon_)

## What Exactly MocomTool is
MocomTool does not enable users to reach LLM models without `API KEYs` which is provided by services. In order to use MocomTool, you need a `.env` file that includes api keys.
You can find a template for the `.env` file named `env_template` in this repo. Check it. The tool is a helper for developers for choosing the best LLM model in their case.

## Giving Basic Prompt and Choosing Model for Comparing
After installing MocomTool from this repo, you will run `mocom.py` in `Terminal`. MocomTool was designed as a CLI App. So you can use it from Terminal easly.
```
(.venv) selcu@macbook-air ~ % python mocom.py
```
