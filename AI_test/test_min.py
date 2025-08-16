import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("🎤 ลองพูดอะไรสักอย่าง...")
        audio = r.listen(source)
        print("กำลังแปลงเสียง...")
        text = r.recognize_google(audio, language="th-TH")
        print("คุณพูดว่า:", text)
except Exception as e:
    print("❌ Error:", e)