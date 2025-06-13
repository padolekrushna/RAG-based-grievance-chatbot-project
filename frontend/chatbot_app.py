import streamlit as st
from chatbot_logic import detect_intent
from api_handler import register_complaint, get_status
from chatbot_logic import call_llm, parse_llm_response
st.title("🛠️ Grievance Chatbot")
st.write("Talk to the bot to register a complaint or check its status.")

if "chat" not in st.session_state:
    st.session_state.chat = []
if "user_details" not in st.session_state:
    st.session_state.user_details = {}

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.chat.append(("user", user_input))
    llm_raw = call_llm(user_input)
    llm_result = parse_llm_response(llm_raw)
    intent = llm_result.get("intent", "unknown")

    if intent == "register":
        # Collect user details step-by-step
        if "name" not in st.session_state.user_details:
            st.session_state.user_details["name"] = st.text_input("Enter your name:")
        if "mobile" not in st.session_state.user_details:
            st.session_state.user_details["mobile"] = st.text_input("Enter your mobile number:")
        if "complaint" not in st.session_state.user_details:
            st.session_state.user_details["complaint"] = st.text_area("Describe your issue:")

        if all(st.session_state.user_details.values()):
            result = register_complaint(
                st.session_state.user_details["name"],
                st.session_state.user_details["mobile"],
                st.session_state.user_details["complaint"]
            )
            bot_response = f"✅ Complaint registered successfully!\nYour Complaint ID: `{result['complaint_id']}`"
            st.session_state.chat.append(("bot", bot_response))
            st.session_state.user_details = {}  # Reset for next conversation

    elif intent == "status":
        mobile = st.text_input("Enter your mobile number to fetch status:")
        if mobile:
            result = get_status(mobile)
            if "error" in result:
                bot_response = "❌ No complaint found for this number."
            else:
                bot_response = f"📦 Complaint ID: {result['complaint_id']} \nStatus: {result['status']}"
            st.session_state.chat.append(("bot", bot_response))

    else:
        st.session_state.chat.append(("bot", "🤖 I'm sorry, I didn't understand that. You can say 'register a complaint' or 'check status'."))

# Display chat
st.markdown("---")
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
