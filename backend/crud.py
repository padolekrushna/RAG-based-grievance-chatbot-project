from database import get_db_connection
from utils import generate_complaint_id

def register_complaint(name, mobile, complaint_text):
    conn = get_db_connection()
    cursor = conn.cursor()
    complaint_id = generate_complaint_id()
    cursor.execute('''
        INSERT INTO complaints (complaint_id, name, mobile, complaint)
        VALUES (?, ?, ?, ?)
    ''', (complaint_id, name, mobile, complaint_text))
    conn.commit()
    conn.close()
    return complaint_id

def get_complaint_status(mobile):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT complaint_id, status FROM complaints
        WHERE mobile = ?
        ORDER BY timestamp DESC LIMIT 1
    ''', (mobile,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"complaint_id": row["complaint_id"], "status": row["status"]}
    return None
