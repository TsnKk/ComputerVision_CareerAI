# ระบบแปลงข้อความเป็นเสียง (Text to Speech) สำหรับแปลงข้อความคำถามที่ gemini สร้างเป็นเสียงสำหรับถามผู้ใช้งาน
import pyttsx3

# เริ่ม engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # ความเร็วในการพูด
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name} - {voice.id}")

# ตั้งเสียงเป็นภาษาไทย
engine.setProperty('voice', 'com.apple.voice.compact.th-TH.Kanya')

# ข้อความที่ต้องการให้พูด

text = input("กรอกข้อความ : ")
engine.say(text)

# เล่นเสียง
engine.runAndWait()
