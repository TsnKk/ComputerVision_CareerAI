import pyttsx3

# เริ่ม engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # ความเร็วในการพูด

# ตั้งเสียงเป็นภาษาไทย
engine.setProperty('voice', 'com.apple.voice.compact.th-TH.Kanya')

# ข้อความที่ต้องการให้พูด

text = input("กรอกข้อความ : ")
engine.say(text)

# เล่นเสียง
engine.runAndWait()
