# NewCareerAI - Advanced Interview System

## 📁 โครงสร้างโฟลเดอร์

### 📂 core/
ไฟล์หลักของระบบสัมภาษณ์งาน
- `interview_system.py` - ระบบสัมภาษณ์งานครบวงจร (AI + TTS + STT)

### 📂 modules/
โมดูลประมวลผลแยกตามหน้าที่
- `STTmodule.py` - ระบบ Speech-to-Text ด้วย Whisper (อัดเสียงอัตโนมัติ)
- `TTSmodule.py` - ระบบ Text-to-Speech ด้วย Google Cloud TTS

### 📂 examples/
ตัวอย่างการใช้งานและทดสอบ
- `google_tts_test.py` - ทดสอบ Google Cloud TTS

### 📂 docs/
เอกสารและคำแนะนำ
- `requirements_note.txt` - รายการสิ่งที่จำเป็น (API Keys)
- `google_tts_notes.txt` - บันทึกเกี่ยวกับ Google TTS

## 🎯 ความสามารถหลัก

- **AI-Powered Interviews**: ใช้ Google Gemini สร้างคำถามจาก JD
- **Premium Voice**: Google Cloud TTS เสียงไทยคุณภาพสูง
- **Smart Recording**: อัดเสียงอัตโนมัติด้วย Whisper
- **Complete Workflow**: JD → คำถาม → สัมภาษณ์ → บันทึกคำตอบ

## 🚀 การใช้งาน

1. ตั้งค่า Environment Variables:
```bash
set GEMINI_API_KEY=your_gemini_api_key
set GOOGLE_APPLICATION_CREDENTIALS=path_to_service_account.json
```

2. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

3. รันระบบสัมภาษณ์:
```bash
python core/interview_system.py
```

## 📋 Dependencies
- google-generativeai (Gemini)
- google-cloud-texttospeech
- whisper
- sounddevice
- scipy
- pygame
