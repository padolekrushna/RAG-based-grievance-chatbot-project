!pip install openai

import os
import openai
from dotenv import load_dotenv
from rag_utils import get_rag_context

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(message, chat_history=None):
    context = get_rag_context(message)

    messages = [{"role": "system", "content": "You are a grievance chatbot. Always respond with JSON: {intent, name, mobile, complaint} or just mobile for status."}]
    if chat_history:
        messages += chat_history
    messages.append({"role": "user", "content": f"Context:\n{context}\n\nMessage:\n{message}"})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def parse_llm_response(text):
    import json
    try:
        return json.loads(text)
    except:
        return {"intent": "unknown"}
