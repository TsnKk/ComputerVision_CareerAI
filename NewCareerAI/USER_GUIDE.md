# 📚 Career AI - Complete User Guide
=====================================

## 🎯 ภาพรวมระบบ
**Career AI** เป็นระบบฝึกสัมภาษณ์งานขั้นสูงที่ขับเคลื่อนด้วย AI สามารถสร้างคำถามสัมภาษณ์ บันทึกเสียง และประเมินการตอบคำถาม

### ฟีเจอร์หลัก
- 🤖 **AI Question Generation** - สร้างคำถามด้วย Google Gemini AI
- 🎤 **Voice Recording** - บันทึกเสียงด้วย Whisper STT
- 🔊 **Text-to-Speech** - แปลงข้อความเป็นเสียงด้วย Google Cloud TTS
- 🌐 **Web Interface** - ใช้งานผ่าน Streamlit
- 💼 **Job Analysis** - วิเคราะห์ Job Description

---

## 🚀 การติดตั้งและเปิดใช้งาน

### ⚡ วิธีเร็ว (แนะนำ)
```bash
# Windows
double-click launch.bat

# Linux/Mac  
bash launch.sh

# Manual
python run_streamlit.py
```

### 🔍 วิธีละเอียด

#### 1. ตรวจสอบระบบ
```bash
python check_requirements.py
```

#### 2. ตั้งค่า API Keys
แก้ไขไฟล์ `.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=careerai-469309-9946c52b3f8e.json
```

#### 3. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

#### 4. เปิดใช้งาน
```bash
python run_streamlit.py
```

### 🌐 การเข้าถึง
- **หลัก**: http://localhost:8501
- **สำรอง**: http://localhost:8502
- **Network**: http://YOUR_IP:8501

---

## 📖 คู่มือการใช้งาน

### การสร้างคำถามสัมภาษณ์
1. เปิดแอพที่ http://localhost:8501
2. กรอก Job Description ในช่องข้อความ
3. กดปุ่ม "สร้างคำถามสัมภาษณ์"
4. รอ AI สร้างคำถาม (5-10 วินาที)

### การบันทึกและตอบคำถาม
1. กดปุ่ม "เริ่มอัดเสียง"
2. พูดคำตอบ (จะหยุดอัตโนมัติเมื่อเงียบ 3 วินาที)
3. ระบบจะแปลงเสียงเป็นข้อความอัตโนมัติ
4. ตรวจสอบคำตอบและแก้ไขหากจำเป็น

### การจัดการไฟล์เสียง
- ไฟล์เสียงจะถูกบันทึกใน `audio_files/`
- สามารถดาวน์โหลดไฟล์เสียงได้
- ระบบจะลบไฟล์เก่าอัตโนมัติ

---

## 🔧 การแก้ไขปัญหา

### ปัญหาที่พบบ่อย

#### 1. Module not found
```bash
pip install -r requirements.txt --force-reinstall
```

#### 2. Port already in use
```bash
# Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8501 | xargs kill -9
```

#### 3. API Key Invalid
1. ตรวจสอบไฟล์ `.env`
2. ตรวจสอบ API key ที่ https://aistudio.google.com/
3. รีสตาร์ทแอพ

#### 4. Microphone Issues
- ตรวจสอบสิทธิ์การเข้าถึงไมโครโฟน
- ลองใช้ไมโครโฟนอื่น
- รีสตาร์ทเบราว์เซอร์

#### 5. TTS ไม่ทำงาน
- ตรวจสอบไฟล์ Google Credentials
- สำหรับ development ใช้ไฟล์จำลองได้
- สำหรับ production ต้องใช้ไฟล์จริงจาก Google Cloud

---

## 🛠️ Google Cloud Setup (ทางเลือก)

### สร้าง Google Cloud Credentials
1. เข้า https://console.cloud.google.com/
2. สร้าง Project ใหม่
3. เปิดใช้ Text-to-Speech API
4. สร้าง Service Account
5. ดาวน์โหลด JSON key
6. วางไฟล์ในโปรเจค

### Gemini API Setup
1. เข้า https://aistudio.google.com/
2. สร้าง API Key
3. เพิ่มใน `.env` file

---

## 📊 ข้อมูลเทคนิค

### System Requirements
- **Python**: 3.8+
- **RAM**: 4GB (แนะนำ 8GB+)
- **Storage**: 2GB ว่าง
- **Internet**: สำหรับ API calls

### Technology Stack
- **Streamlit** - Web framework
- **Google Gemini AI** - Question generation
- **OpenAI Whisper** - Speech-to-text
- **Google Cloud TTS** - Text-to-speech
- **pygame** - Audio playback
- **sounddevice** - Audio recording

### File Structure
```
NewCareerAI/
├── run_streamlit.py         # Main launcher
├── requirements.txt         # Dependencies
├── .env                     # Configuration
├── frontend/
│   └── app_streamlit.py     # Web interface
├── modules/                 # Core modules
├── docs/                    # Documentation
└── audio_files/             # Audio storage
```

---

## ⚡ Quick Commands

### เปิดใช้งานแบบเร็ว
```bash
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"
python run_streamlit.py
```

### ตรวจสอบสถานะ
```bash
python check_requirements.py
curl http://localhost:8501/_stcore/health
```

### หยุดการทำงาน
```bash
# กด Ctrl+C ใน terminal
# หรือ
taskkill /F /IM python.exe
```

---

## 🆘 การขอความช่วยเหลือ

### Log และ Debug
- ข้อมูล error จะแสดงใน terminal
- ตรวจสอบ browser console สำหรับ web errors
- ใช้ `DEBUG=True` ใน `.env` สำหรับข้อมูลเพิ่มเติม

### ติดต่อสนับสนุน
- ตรวจสอบ logs ใน terminal
- รวบรวมข้อมูล error messages
- ระบุขั้นตอนที่เกิดปัญหา

---

**เวอร์ชัน**: 1.0.0  
**อัพเดตล่าสุด**: 23 สิงหาคม 2025  
**สถานะ**: Production Ready

🎯 **พร้อมใช้งาน - เปิดแอพได้ที่ http://localhost:8501**
