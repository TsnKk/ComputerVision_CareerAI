# ComputerVision_CareerAI - โครงสร้างใหม่

## 📁 โครงสร้างโปรเจคโดยรวม

```
ComputerVision_CareerAI/
│
├── 📂 AI_test/           # ระบบ AI สัมภาษณ์งานแบบพื้นฐาน
│   ├── core/             # ไฟล์หลัก
│   │   └── main.py       # ระบบหลัก (STT + Ollama AI + TTS)
│   ├── tests/            # ไฟล์ทดสอบ
│   │   ├── test_min.py   # ทดสอบ STT
│   │   └── test_voice.py # ทดสอบ TTS voices
│   ├── modules/          # โมดูลเพิ่มเติม (ว่าง)
│   └── README.md
│
├── 📂 Career/            # ระบบประมวลผลเสียงด้วย Whisper
│   ├── speech_processing/
│   │   ├── whisper_stt.py     # STT ด้วย Whisper
│   │   └── advanced_whisper.py # STT+TTS ครบวงจร
│   ├── audio_files/
│   │   ├── output.wav    # ไฟล์เสียงผลลัพธ์
│   │   └── recorded.wav  # ไฟล์เสียงที่อัด
│   ├── examples/
│   │   └── simple_tts.py # TTS อย่างง่าย
│   └── README.md
│
├── 📂 Career AI/         # ระบบผู้ช่วยเสียงแบบโมดูลาร์
│   ├── core/
│   │   └── main.py       # ไฟล์หลัก
│   ├── modules/
│   │   ├── ai_module.py  # โมดูล AI (Ollama)
│   │   ├── stt_module.py # โมดูล STT
│   │   ├── tts_module.py # โมดูล TTS
│   │   └── memory.py     # โมดูลความจำ
│   ├── data/
│   │   └── memory.json   # ข้อมูลความจำ
│   ├── config/
│   │   ├── requirements.txt
│   │   ├── setup.sh
│   │   └── คู่มือ.txt
│   ├── __pycache__/
│   └── README.md
│
├── 📂 NewCareerAI/       # ระบบสัมภาษณ์งานขั้นสูง
│   ├── core/
│   │   └── interview_system.py # ระบบสัมภาษณ์หลัก
│   ├── modules/
│   │   ├── STTmodule.py  # Whisper STT
│   │   └── TTSmodule.py  # Google Cloud TTS
│   ├── examples/
│   │   └── google_tts_test.py # ทดสอบ Google TTS
│   ├── docs/
│   │   ├── requirements_note.txt # API Keys ที่จำเป็น
│   │   └── google_tts_notes.txt  # บันทึก TTS
│   ├── file1, .env.example, requirements.txt
│   └── README.md
│
├── 📂 deepface/          # โปรเจค Computer Vision
│   ├── models/
│   │   └── deepface/     # โมเดล DeepFace
│   ├── datasets/
│   │   └── A1/          # ข้อมูลภาพ
│   ├── requirements.txt
│   └── README.md
│
├── how to venv.txt
├── README.md
└── รายละเอียดงาน.txt
```

## 🎯 แยกโฟลเดอร์ตามผู้พัฒนา

### 👤 **AI_test** - นักพัฒนาคนที่ 1
- ระบบ AI สัมภาษณ์งานแบบพื้นฐาน
- ใช้ Speech Recognition + Ollama + macOS TTS

### 👤 **Career** - นักพัฒนาคนที่ 2  
- เน้นการประมวลผลเสียงด้วย Whisper
- ระบบอัดเสียงอัตโนมัติ

### 👤 **Career AI** - นักพัฒนาคนที่ 3
- ระบบผู้ช่วยเสียงแบบโมดูลาร์
- แยกโมดูลชัดเจน พร้อมระบบความจำ

### 👤 **NewCareerAI** - นักพัฒนาคนที่ 4
- ระบบสัมภาษณ์งานขั้นสูงที่สุด
- ใช้ Gemini AI + Google Cloud TTS + Whisper

### 👤 **deepface** - นักพัฒนาคนที่ 5
- โปรเจค Computer Vision สำหรับจดจำใบหน้า

## ✅ การจัดระเบียบที่ทำเสร็จ

1. **แยกโฟลเดอร์ชัดเจน** - แต่ละคนดูแลโฟลเดอร์ของตัวเอง
2. **จัดหมวดหมู่ไฟล์** - แยก core/modules/examples/docs
3. **สร้าง README.md** - แต่ละโฟลเดอร์มีคู่มือการใช้งาน
4. **ชื่อไฟล์ที่เข้าใจง่าย** - เปลี่ยนชื่อให้สื่อความหมาย
5. **โครงสร้างสอดคล้อง** - ใช้รูปแบบเดียวกัน
