#!/usr/bin/env python3
"""
🤖 ai_module.py - Legacy AI Processing Engine
=============================================
ฟีเจอร์หลัก:
- Llama3-based AI processing (Legacy implementation)
- Thai language conversation handling
- Luna AI assistant personality implementation
- Subprocess-based model execution

ความสามารถ:
- AIProcessor class สำหรับ Llama3 model interaction
- Thai language response generation
- English to Thai translation และ processing
- Legacy conversation management

คำเตือน:
- This is a LEGACY module for backward compatibility
- Current system uses Google Gemini AI instead
- Keep for migration และ fallback purposes only
- New implementations should use core/interview_system.py

Status: DEPRECATED - Use Gemini AI in new implementations
การใช้งาน: from modules.ai_module import AIProcessor (Legacy only)
=============================================
"""

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
