# NewCareerAI - Advanced Interview System

## 📁 โครงสร้างโฟลเดอร์

### 📂 core/
ไฟล์หลักของระบบสัมภาษณ์งาน
- `interview_system.py` - ระบบสัมภาษณ์งานครบวงจร (AI + TTS + STT)

### 📂 modules/
โมดูลประมวลผลแยกตามหน้าที่
- `STTmodule.py` - ระบบ Speech-to-Text ด้วย Whisper (อัดเสียงอัตโนมัติ)
- `TTSmodule.py` - ระบบ Text-to-Speech ด้วย Google Cloud TTS
- `config.py` - การตั้งค่าระบบ

### 📂 frontend/
ส่วนแสดงผล Web Interface
- `app_streamlit.py` - เว็บแอปหลักด้วย Streamlit
- `utils.py` - ฟังก์ชันช่วยเหลือสำหรับ UI

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
- **Web Interface**: ใช้งานผ่าน Streamlit Web App
- **Complete Workflow**: JD → คำถาม → สัมภาษณ์ → บันทึก → วิเคราะห์

## 🚀 การใช้งาน

### วิธีที่ 1: ผ่าน Web Interface (แนะนำ)

1. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

2. ตั้งค่า Environment Variables:
```bash
set GEMINI_API_KEY=your_gemini_api_key
set GOOGLE_APPLICATION_CREDENTIALS=path_to_service_account.json
```

3. รัน Streamlit App:
```bash
python run_streamlit.py
```
หรือ
```bash
streamlit run frontend/app_streamlit.py
```

4. เปิดเว็บเบราว์เซอร์ที่: `http://localhost:8501`

### วิธีที่ 2: ผ่าน Command Line

```bash
python main.py
# หรือ
python core/interview_system.py
```

## 🌟 คุณสมบัติเว็บแอป

### 📋 หน้าหลัก
- กรอก Job Description
- สร้างคำถามด้วย AI
- แสดงคำถามที่สร้าง
- ตรวจสอบการตั้งค่าระบบ

### 🎤 ส่วนสัมภาษณ์
- ฟังคำถามด้วยเสียง TTS
- บันทึกคำตอบด้วย STT
- แสดงความคืบหน้า
- นำทางระหว่างคำถาม

### 📊 การวิเคราะห์
- แสดงคำถาม-คำตอบทั้งหมด
- สร้างรายงานวิเคราะห์ด้วย AI
- ส่งออกผลลัพธ์
- เริ่มการสัมภาษณ์ใหม่

### ⚙️ การตั้งค่า
- ตรวจสอบ API Keys
- ทดสอบไมโครโฟน
- ปรับแต่งเสียง TTS
- ดูข้อมูลระบบ

## 📋 Dependencies
- google-generativeai (Gemini)
- google-cloud-texttospeech
- openai-whisper
- sounddevice
- scipy
- pygame
- streamlit

## 🔧 การแก้ไขปัญหา

### ❌ ไม่สามารถใช้ไมโครโฟนได้
- ตรวจสอบสิทธิ์การเข้าถึงไมโครโฟน
- ลองเปลี่ยนไมโครโฟนเริ่มต้น
- ติดตั้ง PyAudio: `pip install pyaudio`

### ❌ เสียง TTS ไม่ออก
- ตรวจสอบไฟล์ Service Account
- ตรวจสอบ GOOGLE_APPLICATION_CREDENTIALS
- ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต

### ❌ Gemini API ไม่ทำงาน
- ตรวจสอบ GEMINI_API_KEY
- ตรวจสอบโควต้า API
- ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต

## 🎉 ข้อดี

1. **ใช้งานง่าย** - Web Interface ที่เป็นมิตร
2. **ทันสมัย** - ใช้ AI เทคโนโลยีล่าสุด
3. **ครบวงจร** - ตั้งแต่สร้างคำถามจนถึงวิเคราะห์
4. **เสียงคุณภาพสูง** - Google Cloud TTS Premium
5. **รองรับภาษาไทย** - เข้าใจและตอบเป็นภาษาไทย
