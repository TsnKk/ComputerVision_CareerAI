#!/bin/bash
echo "🚀 เริ่มต้นการติดตั้งสภาพแวดล้อม AI..."

# อัพเดต Homebrew
brew update

# ติดตั้ง Python 3 และ PortAudio (สำหรับ PyAudio)
brew install python
brew install portaudio

# สร้าง virtual environment ถ้ายังไม่มี
if [ ! -d ".venv" ]; then
  echo "📦 กำลังสร้าง Virtual Environment..."
  python3 -m venv .venv
fi

# เปิดใช้งาน Virtual Environment
source .venv/bin/activate

# สร้างไฟล์ requirements.txt
cat <<EOF > requirements.txt
pyttsx3
SpeechRecognition
pyaudio
sounddevice
numpy
ollama
EOF

# ติดตั้ง dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ ติดตั้งเสร็จสิ้น พร้อมใช้งาน!"
