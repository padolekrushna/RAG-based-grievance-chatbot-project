import requests

BASE_URL = "http://127.0.0.1:8000"

def register_complaint(name, mobile, complaint):
    response = requests.post(f"{BASE_URL}/register", json={
        "name": name,
        "mobile": mobile,
        "complaint": complaint
    })
    return response.json()

def get_status(mobile):
    response = requests.get(f"{BASE_URL}/status", params={"mobile": mobile})
    if response.status_code == 200:
        return response.json()
    return {"error": "No complaint found."}
