from callGemini import call_gemini
from callGPT import call_gpt
from rich.console import Console
from rich.text import Text
import os
import typer

app = typer.Typer()
console = Console()

@app.command()
def compare(prompt:str, gemini: bool=False, claude: bool=False, gpt: bool=False, calculator: bool=False):
    # prompt is being printed to the console
    text_prompt = Text(f"\nprompt: {prompt}")
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
        call_gpt(prompt)
    
    # if gemini is True, call gemini
    if gemini:
        text_gem = Text("\n\nGemini:")
        text_gem.stylize("bold green")
        console.print(text_gem)
        call_gemini(prompt)
        
    if calculator and '*' in prompt:
        text_calc = Text("\n\nCalculator:")
        text_calc.stylize("bold green")
        console.print(text_calc)
        numbers = prompt.split('*')
        print(f"{numbers[0]} * {numbers[1]} = {int(numbers[0])*int(numbers[1])}")
if __name__ == "__main__":
    app()