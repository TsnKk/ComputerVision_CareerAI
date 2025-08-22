# Career - Speech Processing Project

## 📁 โครงสร้างโฟลเดอร์

### 📂 speech_processing/
โมดูลประมวลผลเสียงหลัก
- `whisper_stt.py` - ระบบ Speech-to-Text ด้วย Whisper (อัดเสียงจากไมค์)
- `advanced_whisper.py` - ระบบ STT + TTS แบบครบวงจร (อัดเสียงอัตโนมัติเมื่อเงียบ)

### 📂 audio_files/
ไฟล์เสียงที่ใช้ในการทดสอบ
- `output.wav` - ไฟล์เสียงผลลัพธ์
- `recorded.wav` - ไฟล์เสียงที่อัดจากไมค์

### 📂 examples/
ตัวอย่างการใช้งานง่ายๆ
- `simple_tts.py` - ตัวอย่าง Text-to-Speech อย่างง่าย (pyttsx3)

## 🎯 ความสามารถหลัก

- **Speech-to-Text**: ใช้ Whisper model ถอดเสียงภาษาไทย
- **Text-to-Speech**: รองรับเสียงภาษาไทย macOS
- **Auto Recording**: อัดเสียงอัตโนมัติและหยุดเมื่อเงียบ

## 🚀 การใช้งาน

1. STT ด้วย Whisper:
```bash
python speech_processing/whisper_stt.py
```

2. ระบบครบวงจร:
```bash
python speech_processing/advanced_whisper.py
```

3. TTS อย่างง่าย:
```bash
python examples/simple_tts.py
```

## 📋 Dependencies
- whisper
- sounddevice
- scipy
- numpy
- pyttsx3
