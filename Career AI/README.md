# Career AI - Modular Voice Assistant

## 📁 โครงสร้างโฟลเดอร์

### 📂 core/
ไฟล์หลักของระบบ
- `main.py` - ไฟล์หลักที่รวม modules ทั้งหมด

### 📂 modules/
โมดูลระบบต่างๆ แยกกันชัดเจน
- `ai_module.py` - ระบบ AI (Ollama/Llama3)
- `stt_module.py` - ระบบ Speech-to-Text (Google Speech API)
- `tts_module.py` - ระบบ Text-to-Speech (macOS say command)
- `memory.py` - ระบบจัดเก็บความจำการสนทนา

### 📂 data/
ข้อมูลและไฟล์จัดเก็บ
- `memory.json` - ไฟล์เก็บประวัติการสนทนา

### 📂 config/
ไฟล์การตั้งค่าและเอกสาร
- `requirements.txt` - รายการ Python packages
- `setup.sh` - สคริปต์ตั้งค่าระบบ
- `คู่มือ.txt` - คู่มือการใช้งาน

### 📂 __pycache__/
ไฟล์ Python bytecode (สร้างอัตโนมัติ)

## 🎯 ความสามารถหลัก

- **Modular Design**: แยกโมดูลชัดเจน ง่ายต่อการพัฒนา
- **Voice Assistant**: ระบบผู้ช่วยเสียงภาษาไทย
- **AI Integration**: เชื่อมต่อกับ Ollama/Llama3
- **Memory System**: จัดเก็บประวัติการสนทนา

## 🚀 การใช้งาน

```bash
# ติดตั้ง dependencies
pip install -r config/requirements.txt

# รันระบบหลัก
python core/main.py
```

## 📋 Dependencies
- speech_recognition
- ollama (หรือ subprocess สำหรับ ollama command)
- json (built-in)
- datetime (built-in)
