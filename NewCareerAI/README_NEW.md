# 🚀 Career AI - AI-Powered Interview Coach
===============================================

> **ระบบฝึกสัมภาษณ์งานขั้นสูงด้วย AI**  
> สร้างคำถามสัมภาษณ์ บันทึกเสียง และประเมินการตอบด้วยเทคโนโลยี AI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-green.svg)](#)

## ⚡ Quick Start

### 🎯 เปิดใช้งานแบบเร็ว
```bash
# Windows - Double-click
launch.bat

# Linux/Mac
bash launch.sh

# Manual
python run_streamlit.py
```

**➡️ เปิดเบราว์เซอร์ไปที่: http://localhost:8501**

---

## 🌟 ฟีเจอร์หลัก

| ฟีเจอร์ | เทคโนโลยี | สถานะ |
|---------|-----------|-------|
| 🤖 **AI Question Generation** | Google Gemini AI | ✅ Ready |
| 🎤 **Voice Recording** | OpenAI Whisper | ✅ Ready |
| 🔊 **Text-to-Speech** | Google Cloud TTS | ⚠️ Config Required |
| 🌐 **Web Interface** | Streamlit | ✅ Ready |
| 💼 **Job Analysis** | AI Processing | ✅ Ready |

---

## 📋 System Requirements

- **Python 3.8+**
- **RAM 4GB** (แนะนำ 8GB+)
- **Storage 2GB** ว่าง
- **Internet** สำหรับ API calls

---

## 🛠️ Installation

### 1. Clone Repository
```bash
git clone [repository-url]
cd NewCareerAI
```

### 2. Setup Environment
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
# Copy and edit .env file
cp .env.example .env
```

แก้ไขไฟล์ `.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
```

### 4. Launch Application
```bash
python run_streamlit.py
```

---

## 📖 Documentation

| เอกสาร | เนื้อหา | เหมาะสำหรับ |
|--------|---------|-------------|
| **[USER_GUIDE.md](USER_GUIDE.md)** | คู่มือการใช้งานครบถ้วน | ผู้ใช้ทั่วไป |
| **[DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)** | คู่มือพัฒนาระบบ | นักพัฒนา |
| **[docs/google_credentials_setup.md](docs/google_credentials_setup.md)** | การตั้งค่า Google Cloud | Admin |

---

## 🏗️ Architecture

```
Career AI System
├── 🌐 Web Interface (Streamlit)
├── 🤖 AI Engine (Google Gemini)
├── 🎤 Speech-to-Text (Whisper)
├── 🔊 Text-to-Speech (Google Cloud)
└── 💾 File Management (Local Storage)
```

---

## 🧪 Development

### Testing
```bash
python check_requirements.py  # System validation
python check_api_keys.py      # API testing
python test_imports.py        # Module testing
```

### Development Server
```bash
streamlit run frontend/app_streamlit.py --server.port 8501
```

---

## 🔧 Troubleshooting

### Common Issues

**Port already in use:**
```bash
taskkill /F /IM python.exe  # Windows
lsof -ti:8501 | xargs kill -9  # Linux/Mac
```

**Module not found:**
```bash
pip install -r requirements.txt --force-reinstall
```

**API Key errors:** 
- ตรวจสอบไฟล์ `.env`
- ตรวจสอบ API key ที่ https://aistudio.google.com/

➡️ **รายละเอียดเพิ่มเติม**: [USER_GUIDE.md](USER_GUIDE.md#การแกไขปญหา)

---

## 📊 Project Stats

- **Total Files**: 40+ files
- **Python Modules**: 15+ modules  
- **Documentation**: 3 main guides
- **Features**: 5+ core features
- **Status**: Production Ready

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

➡️ **รายละเอียด**: [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md#contributing-guidelines)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

- 📖 **Documentation**: [USER_GUIDE.md](USER_GUIDE.md)
- 👨‍💻 **Development**: [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)
- 🐛 **Issues**: Create GitHub issue
- 💬 **Discussions**: GitHub Discussions

---

**Made with ❤️ by Career AI Team**  
**Version**: 1.0.0 | **Updated**: August 23, 2025
