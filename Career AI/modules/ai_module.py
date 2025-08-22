import subprocess
import json

class AIProcessor:
    def __init__(self, model="llama3"):
        self.model = model

    def get_response(self, text):
        prompt = f"""
        คุณคือลูน่า (Luna) ผู้ช่วยอัจฉริยะ ให้ตอบเป็นภาษาไทยเสมอ 
        ถ้าเจอข้อความที่เป็นภาษาอังกฤษ ให้แปลเป็นภาษาไทยแล้วตอบ
        คำถามของผู้ใช้คือ: "{text}"
        """
        try:
            response = subprocess.check_output(
                ["ollama", "run", self.model],
                input=prompt.encode("utf-8"),
                text=True
            )
            return response.strip()
        except Exception as e:
            return f"⚠️ เกิดข้อผิดพลาด: {e}"