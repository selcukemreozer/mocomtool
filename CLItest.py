import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")
    
@app.command()
def deneme(name: str, test: bool = False):
    print(f"Hello {name}")
    if test:
        print("Test mode is on")
        
if __name__ == "__main__":
    app()
