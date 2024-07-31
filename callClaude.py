import anthropic
import os

def call_claude(prompt, max_tokens=400):
    claudeapi: str = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=claudeapi)
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=f"Human: {prompt}\n\nAssistant:",
        max_tokens_to_sample=max_tokens
    )
    
    return response.completion