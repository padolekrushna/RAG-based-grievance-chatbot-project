import streamlit as st
from chatbot_logic import call_llm, parse_llm_response
import requests

st.set_page_config(page_title="Grievance Chatbot", layout="centered")
st.title("📨 Grievance Assistant (RAG + OpenAI)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your complaint or ask status...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    llm_raw = call_llm(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": llm_raw})

    response = parse_llm_response(llm_raw)
    intent = response.get("intent", "unknown")

    if intent == "register":
        # Send to FastAPI backend (replace URL with real one if needed)
        res = requests.post("http://localhost:8000/register", json=response)
        if res.status_code == 200:
            complaint_id = res.json().get("complaint_id")
            msg = f"✅ Complaint registered. Your ID: `{complaint_id}`"
        else:
            msg = "❌ Failed to register complaint."
        st.session_state.chat_history.append({"role": "assistant", "content": msg})

    elif intent == "status":
        res = requests.get("http://localhost:8000/status", params={"mobile": response.get("mobile")})
        status = res.json().get("status", "Not Found")
        msg = f"📌 Complaint Status: `{status}`"
        st.session_state.chat_history.append({"role": "assistant", "content": msg})

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
