import anthropic
import os
def call_claude(prompt):
    claudeapi: str = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=claudeapi,
    )
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
