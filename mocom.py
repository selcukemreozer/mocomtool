from modelsConfig import call_gemini, call_claude, call_groq, call_ollama, call_gpt, CALL_ALL_MODELS
from rich.console import Console
from rich.text import Text
import typer
import json as js
from terminal import clear_terminal, position
from fileprocess import create_json_file, write_to_json
from introduce import Introduce
from time import time
# from tiktoken 

clear_terminal()

app = typer.Typer()
console = Console()

# to prevent confusion, program will call the models in this function
# and get the scores of the models from the user to save in the json file
def callMultimodel(newFileName:str,prompt:str, all: bool=False,
                   gemini: bool=False, claude: bool=False, gpt: bool=False,
                   calculator: bool=False, 
                   ollama: bool=False, groq: bool=False, 
                   promptnumber: int=0) -> dict:

    modelDict = { # the dictionary that holds which models were called and their functions
        "gpt"       : [gpt, call_gpt      ],
        "gemini"    : [gemini, call_gemini],
        "claude"    : [claude,call_claude ],
        "calculator": [calculator,print   ], # calculator is not ready yet
        "groq"      : [groq, call_groq    ],
        "ollama"    : [ollama, call_ollama],
                }  

    if all: # if <all> is called, call all the models that are chosen 
        for each in CALL_ALL_MODELS.keys():
            modelDict[each][0] = CALL_ALL_MODELS[each]
      
    # prompt is being printed to the console
    text_prompt = Text(f"\nprompt {['' if promptnumber == 0 else promptnumber][0]}: {prompt}")
    text_prompt.stylize("bold red",0,10)
    console.print(text_prompt)
    
    currentPromptDict = {f"prompt{promptnumber}": {"prompt": prompt}}
    list_of_responses = dict()
    
    for modelName in modelDict:

        if modelDict[modelName][0]:
            # if the model is called, print the model name
            text_model = Text(f"\n{modelName}:")
            text_model.stylize("bold green")
            console.print(text_model)
            
            start = time()
            call_LLM = modelDict[modelName][1] # get the model function ex: call_gemini
            modelANDresponse = call_LLM(prompt) # call the model function with the prompt
            end = time()
            
            theResponse = modelANDresponse[0]
            # print the response and the time taken to get the response
            print(theResponse)
            console.print(f"\n  Time taken: {round(end-start,3)} seconds")
            
            modelVersion = Text(f"  Model:{modelANDresponse[1]}\n") # like gemma2:2b
            modelVersion.stylize("bright_magenta",8)
            console.print(modelVersion)
            
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
def compare(info:str, all: bool=False, gemini: bool=False, claude: bool=False, 
            gpt: bool=False, calculator: bool=False, 
            ollama: bool=False, groq: bool=False, json: bool=False):
    
    if json:
        # if the prompt is a json file with multiple prompts, 
        # read the file and call the models for each prompt
        file = open(info, 'r')
        data = js.load(file)
        
        newFile = input("Do you want to save the responses in a new json file? (y/n): ")
        if newFile == 'y':
            jsonfileName = input("Enter the name of the json file: ") + ".json"
            create_json_file(jsonfileName)
            
            for index, prompt in enumerate(data):
                results = callMultimodel(newFileName=jsonfileName,prompt=data[prompt]["prompt"], all=all, gemini=gemini, claude=claude, gpt=gpt, ollama=ollama, groq=groq, calculator=calculator, promptnumber = index+1)
                write_to_json(jsonfileName, results)
                clear_terminal()
        else:
            for index, prompt in enumerate(data):
                callMultimodel(newFileName='',prompt=data[prompt]["prompt"], all=all, gemini=gemini, claude=claude, gpt=gpt, qroq=groq, ollama=ollama, calculator=calculator, promptnumber = index+1)
                clear_terminal()
    else:
        # if the prompt is a single prompt, 
        # call the models for just one prompt and info is the prompt, not a file
        callMultimodel(newFileName='', prompt=info, all=all, gemini=gemini, claude=claude, gpt=gpt, ollama=ollama, groq=groq, calculator=calculator)
        
@app.command()
def introduce():
    Introduce()
    
if __name__ == "__main__":
    app()