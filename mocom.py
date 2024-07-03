from callGemini import call_gemini
from callGPT import call_gpt
from rich.console import Console
from rich.text import Text
import os
import typer
import json

app = typer.Typer()
console = Console()

def callMultimodel(info:str, gemini: bool=False, claude: bool=False, gpt: bool=False, calculator: bool=False, promptnumber: int=0):
        # prompt is being printed to the console
        text_prompt = Text(f"\nprompt{promptnumber}: {info}")
        text_prompt.stylize("bold red",0,8)
        console.print(text_prompt)
        # if claude is True, call claude
        if claude:
            text_anth = Text("\nClaude 3.5:")
            text_anth.stylize("bold green")
            console.print(text_anth)
            print("claude 3.5 is not implemented yet")
        
        # if gpt is True, call gpt
        if gpt:
            text_open = Text("\n\nchatGPT:")
            text_open.stylize("bold green")
            console.print(text_open)
            call_gpt(info)
        
        # if gemini is True, call gemini
        if gemini:
            text_gem = Text("\n\nGemini:")
            text_gem.stylize("bold green")
            console.print(text_gem)
            call_gemini(info)
            
        if calculator and '*' in info:
            text_calc = Text("\n\nCalculator:")
            text_calc.stylize("bold green")
            console.print(text_calc)
            numbers = info.split('*')
            print(f"{numbers[0]} * {numbers[1]} = {int(numbers[0])*int(numbers[1])}")
        
        

@app.command()
def introduce():
    text_intro = Text("\nMocomTool:")
    text_intro.stylize("bold red")
    console.print(text_intro)
    print("MocomTool is a CLI tool that allows you to compare the responses of different models to a given prompt.")
    print(("_"*20)+"\n\nYou can compare the responses of OpenAI's GPT-3.5-turbo model, Google's Gemini-1.5-flash model, and a calculator.")
    print(("_"*20)+"\n\nYou can also compare the responses of Claude 3.5, but it is not implemented yet.")
    print(("_"*20)+"\n\nYou can use the \n[\n --gemini\n --claude\n --gpt\n --calculator(it just can multiply)\n]\n flags to specify which models you want to compare.")
    print(("_"*20)+"\n\nYou can use the [--help] flag to get more information about the available flags.")
    print(("_"*20)+"\n\nYou can use the [--introduce] flag to get a brief introduction to Mocom.")
    print(("_"*20)+"\n\nYou can use the [--compare] flag to compare the responses of the models to a given prompt.")
    print("\n\n[--calculator] flag is just for multiplying two numbers for now.")    

@app.command()
def compare(info:str, gemini: bool=False, claude: bool=False, gpt: bool=False, calculator: bool=False, mprompt: bool=False):
    
    if mprompt: 
        # if the prompt is a json file with multiple prompts, 
        # read the file and call the models for each prompt
        file = open(info, 'r')
        data = json.load(file)
        for index, prompt in enumerate(data):
            callMultimodel(data[prompt]["prompt"], gemini, claude, gpt, calculator, promptnumber = index+1)
    else:
        # if the prompt is a single prompt, 
        # call the models for just one prompt and info is the prompt not a file
        callMultimodel(info, gemini, claude, gpt, calculator, promptnumber = 1)
if __name__ == "__main__":
    app()