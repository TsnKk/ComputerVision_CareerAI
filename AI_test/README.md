# AI Test Project

## 📁 โครงสร้างโฟลเดอร์

### 📂 core/
ไฟล์หลักของระบบ AI สัมภาษณ์งาน
- `main.py` - ไฟล์หลักที่รวมทุกระบบเข้าด้วยกัน (Speech Recognition + Ollama AI + Text-to-Speech)

### 📂 tests/
ไฟล์ทดสอบระบบต่างๆ
- `test_min.py` - ทดสอบระบบ Speech Recognition อย่างง่าย
- `test_voice.py` - ทดสอบเสียง pyttsx3 voices

### 📂 modules/
(สำหรับเก็บ modules เพิ่มเติมในอนาคต)

## 🚀 การใช้งาน

1. รันไฟล์หลัก:
```bash
python core/main.py
```

2. ทดสอบระบบ:
```bash
python tests/test_min.py      # ทดสอบ STT
python tests/test_voice.py    # ทดสอบ TTS
```

## 📋 Dependencies
- speech_recognition
- ollama
- pyttsx3 (สำหรับ macOS)
