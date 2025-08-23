# ⚡ Quick Start Commands

## 🚀 Instant Launch (Copy & Paste)

### Windows PowerShell
```powershell
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"; python run_streamlit.py
```

### Windows Command Prompt
```cmd
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI" && python run_streamlit.py
```

### Auto-Setup Windows Batch
```cmd
double-click launch.bat
```

---

## 🎯 Essential Commands

### Check Everything is Ready
```powershell
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"
python --version
pip list | findstr streamlit
dir requirements.txt
dir run_streamlit.py
type .env
```

### Install Missing Dependencies
```powershell
pip install streamlit google-generativeai openai-whisper pygame sounddevice python-dotenv
```

### Force Reinstall Everything
```powershell
pip install -r requirements.txt --force-reinstall --no-cache-dir
```

---

## 🌐 Access URLs

### Primary Access
- http://localhost:8501

### Alternative Ports
- http://localhost:8502
- http://localhost:8503

### Network Access
- http://172.20.28.42:8501 (or your IP)

---

## 🔧 Troubleshooting One-Liners

### Kill All Python Processes
```powershell
taskkill /F /IM python.exe
```

### Check Port Usage
```powershell
netstat -ano | findstr :8501
```

### Restart Fresh
```powershell
taskkill /F /IM python.exe; cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"; python run_streamlit.py
```

### Test API Key
```powershell
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Key:', os.getenv('GEMINI_API_KEY')[:10] + '...' if os.getenv('GEMINI_API_KEY') else 'Not found')"
```

---

## 📱 Mobile Quick Commands

### Copy-Paste Launch Command
```
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"; python run_streamlit.py
```

### Environment Check
```
python --version && pip --version && echo "Ready!"
```

### Full Reset & Launch
```
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI" && pip install -r requirements.txt && python run_streamlit.py
```

---

## 🎨 Status Check Commands

### Quick Health Check
```powershell
# Test if app is running
curl http://localhost:8501/_stcore/health
```

### Full System Status
```powershell
echo "=== Python ==="
python --version

echo "=== Project Files ==="
dir *.py | findstr /i "run_streamlit\|requirements"

echo "=== Environment ==="
type .env | findstr GEMINI_API_KEY

echo "=== Packages ==="
pip list | findstr /i "streamlit\|google\|whisper"

echo "=== Ports ==="
netstat -ano | findstr :8501
```

---

## 🏃‍♂️ Emergency Recovery

### Complete Reset
```powershell
# Stop everything
taskkill /F /IM python.exe

# Clean install
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"
pip uninstall streamlit -y
pip install streamlit
pip install -r requirements.txt

# Launch
python run_streamlit.py
```

### Minimal Launch (Skip checks)
```powershell
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI\frontend"
streamlit run app_streamlit.py --server.port 8501 --server.headless true
```

---

## 💡 Pro Tips

### Background Launch
```powershell
start /B python run_streamlit.py
```

### Launch with Log
```powershell
python run_streamlit.py > streamlit.log 2>&1
```

### Launch Different Port
```powershell
python -c "import streamlit.cli as stcli; import sys; sys.argv = ['streamlit', 'run', 'frontend/app_streamlit.py', '--server.port', '8502']; stcli.main()"
```

---

**⚡ สำหรับการใช้งานทั่วไป ให้ copy คำสั่งนี้:**
```powershell
cd "C:\Users\Admin\Documents\GitHub\ComputerVision_CareerAI\NewCareerAI"; python run_streamlit.py
```
