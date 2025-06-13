import uuid

def generate_complaint_id():
    return "CMP" + str(uuid.uuid4().hex[:6].upper())
