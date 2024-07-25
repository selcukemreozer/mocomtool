from callGemini import call_gemini
from callGPT import call_gpt
from rich.console import Console
from rich.text import Text
import typer
import json
from terminal import clear_terminal, position
from fileprocess import create_json_file, write_to_json
from introduce import Introduce
from time import time

clear_terminal()

app = typer.Typer()
console = Console()

# to prevent confusion, program will call the models in this function
# and get the scores of the models from the user to save in the json file
def callMultimodel(newFileName:str,prompt:str, gemini: bool=False, claude: bool=False, gpt: bool=False, calculator: bool=False, promptnumber: int=0):
    # prompt is being printed to the console
    text_prompt = Text(f"\nprompt {['' if promptnumber == 0 else promptnumber][0]}: {prompt}")
    text_prompt.stylize("bold red",0,10)
    console.print(text_prompt)
    
    modelDict = { # the dictionary that holds which models were called and their functions
        "gemini": [gemini, call_gemini],
        "gpt":    [gpt, call_gpt],
        "claude": [claude,print],
        "calculator": [calculator,print] # calculator is not ready yet
                 }
    currentPromptDict = {f"prompt{promptnumber}": {"prompt": prompt}}
    list_of_responses = dict()
    
    for modelName in modelDict:
        
        if modelDict[modelName][0]:
            text_model = Text(f"\n{modelName}:")
            text_model.stylize("bold green")
            console.print(text_model)
            start = time()
            theResponse = modelDict[modelName][1](prompt) # call the model function with the prompt
            end = time()
            print(theResponse)
            console.print(f"\n{modelName}, Time taken: {round(end-start)}")
            list_of_responses.update( # save the responses in a dictionary
                {
                modelName: theResponse   
                })
    if promptnumber != 0: # if there are more prompts, ask the user to rate the models
        currentPromptDict[f"prompt{promptnumber}"].update({"responses":list_of_responses})
        # above code saves the responses of the models in the dictionary list_of_responses
        
        scores = dict()
        
        for modelName in list_of_responses:
            
            scores.update({
                modelName: int(input(f"Rate the {modelName}(1-9): "))
                })
            
        currentPromptDict[f"prompt{promptnumber}"].update({"scores": scores})
        return currentPromptDict
            
@app.command()
def compare(info:str, gemini: bool=False, claude: bool=False, gpt: bool=False, calculator: bool=False, json: bool=False):
    
    if json:
        # if the prompt is a json file with multiple prompts, 
        # read the file and call the models for each prompt
        file = open(info, 'r')
        data = json.load(file)
        
        newFile = input("Do you want to save the responses in a new json file? (y/n): ")
        if newFile == 'y':
            jsonfileName = input("Enter the name of the json file: ") + ".json"
            create_json_file(jsonfileName)
            
            for index, prompt in enumerate(data):
                results = callMultimodel(newFileName=jsonfileName,prompt=data[prompt]["prompt"], gemini=gemini, claude=claude, gpt=gpt, calculator=calculator, promptnumber = index+1)
                write_to_json(jsonfileName, results)
                clear_terminal()
        else:
            for index, prompt in enumerate(data):
                callMultimodel(newFileName='',prompt=data[prompt]["prompt"], gemini=gemini, claude=claude, gpt=gpt, calculator=calculator, promptnumber = index+1)
                clear_terminal()
    else:
        # if the prompt is a single prompt, 
        # call the models for just one prompt and info is the prompt, not a file
        callMultimodel(newFileName='', prompt=info, gemini=gemini, claude=claude, gpt=gpt, calculator=calculator)
        
@app.command()
def introduce():
    Introduce()
    
if __name__ == "__main__":
    app()