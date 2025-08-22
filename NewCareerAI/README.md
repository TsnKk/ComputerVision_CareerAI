# NewCareerAI - ระบบสัมภาษณ์งานอัตโนมัติ

ระบบสัมภาษณ์งานที่ใช้ AI สร้างคำถามจาก Job Description, อ่านคำถามด้วยเสียง, และบันทึก-ถอดเสียงคำตอบ

## 🔧 การติดตั้ง

### 1. สร้าง Virtual Environment
```powershell
cd NewCareerAI
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. ติดตั้งไลบรารี
```powershell
pip install -r requirements.txt
```

### 3. ตั้งค่า Environment Variables

สร้างไฟล์ `.env` จากตัวอย่าง:
```powershell
copy .env.example .env
```

แก้ไขไฟล์ `.env`:
```
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
GEMINI_API_KEY=your_gemini_api_key_here
```

**หรือ** ตั้งค่าใน PowerShell:
```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="path\to\your\service-account-key.json"
$env:GEMINI_API_KEY="your_gemini_api_key_here"
```

## 📁 ไฟล์หลัก

- `test.py` - ระบบสัมภาษณ์หลัก
- `TTSmodule.py` - Text-to-Speech (Google Cloud TTS + pygame)
- `STTmodule.py` - Speech-to-Text (Whisper + sounddevice)
- `soundTest.py` - ทดสอบ Google TTS

## 🚀 การใช้งาน

```powershell
python test.py
```

1. กรอก Job Description
2. ระบบจะสร้างคำถามด้วย Gemini AI
3. อ่านคำถามด้วยเสียง (Google TTS)
4. อัดเสียงคำตอบ (Whisper STT)
5. แสดงผลคำตอบทั้งหมด

## 🔑 การขอ API Keys

### Google Cloud Text-to-Speech
1. ไป [Google Cloud Console](https://console.cloud.google.com/)
2. สร้างโปรเจคใหม่
3. เปิดใช้งาน Text-to-Speech API
4. สร้าง Service Account และดาวน์โหลด JSON key
5. ตั้งค่า `GOOGLE_APPLICATION_CREDENTIALS`

### Gemini API
1. ไป [Google AI Studio](https://aistudio.google.com/)
2. สร้าง API key
3. ตั้งค่า `GEMINI_API_KEY`

## 📋 ไลบรารีที่ใช้

- `google-generativeai` - Gemini AI
- `google-cloud-texttospeech` - Google TTS
- `openai-whisper` - Speech-to-Text
- `sounddevice`, `numpy`, `scipy` - การบันทึกเสียง
- `pygame` - เล่นไฟล์เสียง
- `playsound` - เล่นไฟล์เสียง (สำรอง)
