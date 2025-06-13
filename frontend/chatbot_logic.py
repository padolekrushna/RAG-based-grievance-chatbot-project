def detect_intent(message):
    message = message.lower()
    if "register" in message or "complaint" in message or "issue" in message:
        return "register"
    elif "status" in message:
        return "status"
    return "unknown"
