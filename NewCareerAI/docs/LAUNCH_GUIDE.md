# 🚀 คู่มือการเปิดตัว Career AI - Streamlit Application

## 📋 สิ่งที่จำเป็นก่อนการใช้งาน (Prerequisites)

### 1. Python Environment
- **Python 3.8+** (แนะนำ Python 3.9-3.11)
- **pip** (Python package manager)
- **Virtual Environment** (แนะนำ)

### 2. API Keys และ Credentials
- **Gemini API Key** (จาก Google AI Studio)
- **Google Cloud Credentials** (สำหรับ Text-to-Speech - Optional)

### 3. System Requirements
- **Windows 10/11** หรือ **macOS/Linux**
- **RAM**: อย่างน้อย 4GB (แนะนำ 8GB+)
- **Storage**: อย่างน้อย 2GB ว่าง
- **Internet Connection** (สำหรับ API calls)

---

## 🛠️ ขั้นตอนการติดตั้งและเปิดตัว

### Step 1: ตรวจสอบ Python
```powershell
python --version
pip --version
```

### Step 2: เปลี่ยนไปยังโฟลเดอร์โปรเจค
```powershell
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"
```

### Step 3: ติดตั้ง Dependencies
```powershell
pip install -r requirements.txt
```

### Step 4: ตั้งค่า Environment Variables
สร้างหรือแก้ไขไฟล์ `.env`:
```env
# Gemini API Key (จำเป็น)
GEMINI_API_KEY=your_gemini_api_key_here

# Google Cloud Credentials (ทางเลือก)
GOOGLE_APPLICATION_CREDENTIALS=careerai-469309-9946c52b3f8e.json

# Optional Settings
DEBUG=False
PORT=8501
```

### Step 5: เปิดตัวแอพพลิเคชัน
```powershell
python run_streamlit.py
```

---

## 🎯 วิธีการใช้งานแบบ Quick Start

### วิธีที่ 1: One-Command Launch
```powershell
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI" && python run_streamlit.py
```

### วิธีที่ 2: Manual Streamlit
```powershell
cd frontend
streamlit run app_streamlit.py --server.port 8501
```

### วิธีที่ 3: Background Mode
```powershell
start python run_streamlit.py
```

---

## 📂 โครงสร้างไฟล์ที่สำคัญ

```
NewCareerAI/
├── 📄 run_streamlit.py          # Main launcher
├── 📄 requirements.txt         # Dependencies
├── 📄 .env                     # Environment variables
├── 📁 frontend/
│   ├── 📄 app_streamlit.py     # Streamlit app
│   ├── 📄 utils.py             # Utilities
│   └── 📄 .env                 # Frontend env
├── 📁 modules/
│   ├── 📄 config.py            # Configuration
│   ├── 📄 STTmodule.py         # Speech-to-Text
│   └── 📄 TTSmodule.py         # Text-to-Speech
├── 📁 core/
│   └── 📄 interview_system.py  # Core logic
└── 📁 audio_files/             # Audio storage
```

---

## ⚡ Quick Commands

### รันแอพ
```powershell
cd NewCareerAI && python run_streamlit.py
```

### ตรวจสอบสถานะ
```powershell
curl http://localhost:8501
```

### หยุดแอพ
```powershell
# กด Ctrl+C ใน terminal
# หรือ
taskkill /F /IM python.exe
```

---

## 🔧 การแก้ไขปัญหาเบื้องต้น

### ปัญหา: Module not found
```powershell
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### ปัญหา: Port already in use
```powershell
# ค้นหา process ที่ใช้ port 8501
netstat -ano | findstr :8501
# หยุด process
taskkill /PID <PID_NUMBER> /F
```

### ปัญหา: API Key Invalid
1. ตรวจสอบไฟล์ `.env`
2. ตรวจสอบ API key ใน Google AI Studio
3. รีสตาร์ทแอพ

### ปัญหา: Google Credentials
1. ใช้ไฟล์จำลองที่มีอยู่ (TTS จะไม่ทำงาน)
2. หรือสร้างไฟล์จริงจาก Google Cloud Console

---

## 🌐 URLs และ Endpoints

### Development URLs
- **Local**: http://localhost:8501
- **Network**: http://172.20.28.42:8501 (หรือ IP ของเครื่อง)

### Health Check
- **Status**: http://localhost:8501/_stcore/health

---

## 🎛️ การปรับแต่งขั้นสูง

### เปลี่ยน Port
แก้ไขใน `run_streamlit.py`:
```python
port = 8502  # เปลี่ยนจาก 8501
```

### เปิด Debug Mode
แก้ไขใน `.env`:
```env
DEBUG=True
```

### ปรับแต่ง Whisper Model
แก้ไขใน `modules/config.py`:
```python
model_size = "medium"  # tiny, base, small, medium, large
```

---

## 📊 ฟีเจอร์ที่พร้อมใช้งาน

### ✅ ฟีเจอร์ที่ทำงาน
- 🤖 **AI Question Generation** (Gemini AI)
- 🎤 **Speech Recording** (Whisper STT)  
- 💾 **Audio File Management**
- 🎯 **Interview Simulation**
- 📝 **Job Description Analysis**

### ⚠️ ฟีเจอร์ที่ต้องการ Setup เพิ่ม
- 🔊 **Text-to-Speech** (ต้องมี Google Cloud Credentials จริง)

---

## 🆘 การขอความช่วยเหลือ

### Log Files
- ตรวจสอบ terminal output
- ไฟล์ log จะแสดงใน console

### Common Issues
1. **ImportError**: ติดตั้ง requirements.txt
2. **API Error**: ตรวจสอบ API keys
3. **Port Error**: เปลี่ยน port หรือหยุด process อื่น
4. **Path Error**: ตรวจสอบ working directory

---

## 📞 Support Information

**Project**: NewCareerAI - AI Interview Coach
**Version**: 1.0.0
**Last Updated**: August 23, 2025
**Platform**: Streamlit Web Application

---

*🎯 เมื่อทำตามขั้นตอนแล้ว แอพจะเปิดที่ http://localhost:8501 อัตโนมัติ*
