# 📋 Pre-Launch Checklist

## ✅ ระบบพร้อมใช้งาน (System Ready)

### Python Environment
- [ ] Python 3.8+ installed
- [ ] pip package manager available
- [ ] Virtual environment activated (recommended)

### Project Files
- [x] `requirements.txt` exists
- [x] `run_streamlit.py` exists
- [x] `frontend/app_streamlit.py` exists
- [x] All module files present

### API Keys & Credentials
- [ ] Gemini API Key configured in `.env`
- [ ] Google Cloud Credentials (optional for TTS)

### Dependencies
- [ ] All Python packages installed (`pip install -r requirements.txt`)

### Directories
- [x] `audio_files/` directory exists
- [x] `frontend/` directory exists
- [x] `modules/` directory exists

## 🚀 Launch Methods

### Method 1: Auto Launch Script (Windows)
```batch
double-click launch.bat
```

### Method 2: Auto Launch Script (Linux/Mac)
```bash
bash launch.sh
```

### Method 3: Manual Command
```bash
cd NewCareerAI
python run_streamlit.py
```

### Method 4: Direct Streamlit
```bash
cd NewCareerAI/frontend
streamlit run app_streamlit.py --server.port 8501
```

## 🎯 Expected Output

### Successful Launch
```
============================================================
🚀 เริ่มต้น AI Coach for Interview
============================================================
✅ Streamlit พร้อมใช้งาน
📁 เส้นทางแอป: .../frontend/app_streamlit.py
🌐 กำลังเปิดเว็บเบราว์เซอร์...
📍 URL: http://localhost:8501

  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://YOUR_IP:8501

✅ โหลดการตั้งค่าจาก .env
✅ โหลดโมเดล Whisper สำเร็จ
```

### Available URLs
- **Primary**: http://localhost:8501
- **Alternative**: http://localhost:8502
- **Network**: http://YOUR_IP:8501

## 🔧 Troubleshooting

### Issue: Module Not Found
**Solution**: 
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: Port Already in Use
**Windows**:
```batch
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

**Linux/Mac**:
```bash
lsof -ti:8501 | xargs kill -9
```

### Issue: API Key Invalid
**Solution**:
1. Check `.env` file
2. Verify API key from Google AI Studio
3. Restart application

### Issue: Permission Denied
**Solution**:
```bash
chmod +x launch.sh  # Linux/Mac only
```

## 📊 Feature Status

### ✅ Working Features
- AI Question Generation (Gemini)
- Speech Recording (Whisper STT)
- Audio File Management
- Web Interface (Streamlit)
- Job Description Analysis

### ⚠️ Limited Features
- Text-to-Speech (requires real Google credentials)

## 🎛️ Configuration Files

### `.env` Template
```env
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=careerai-469309-9946c52b3f8e.json
DEBUG=False
PORT=8501
```

### Port Configuration
- Default: 8501
- Alternative: 8502
- Custom: Edit `run_streamlit.py`

## 📞 Support

### Common Commands
```bash
# Check status
curl http://localhost:8501/_stcore/health

# Stop application
Ctrl+C (in terminal)
taskkill /F /IM python.exe (Windows force stop)

# Restart
python run_streamlit.py
```

### Log Locations
- Terminal output (real-time)
- Streamlit logs (in terminal)
- Error messages (console)

---

**Last Updated**: August 23, 2025
**Status**: ✅ Ready for Launch
