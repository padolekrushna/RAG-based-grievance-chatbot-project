!pip install openai

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("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")

def call_llm(message, chat_history=None):
    messages = [{"role": "system", "content": "You are a helpful grievance assistant. Understand the user's intent (register complaint or check status) and extract name, mobile, complaint when relevant."}]
    
    if chat_history:
        messages += chat_history
    
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4
        messages=messages,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def parse_llm_response(llm_output):
    """
    LLM should return a structure like:
    {
        "intent": "register",
        "name": "John",
        "mobile": "9876543210",
        "complaint": "My laptop is overheating"
    }
    """
    import json
    try:
        return json.loads(llm_output)
    except json.JSONDecodeError:
        return {"intent": "unknown"}
