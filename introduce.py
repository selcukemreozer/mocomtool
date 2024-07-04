from rich.console import Console
from rich.text import Text
console = Console()

def Introduce() :
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
