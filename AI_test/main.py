import speech_recognition as sr
import ollama
import subprocess

CHARACTER_PROMPT = """
คุณเป็นคนที่คอยสัมภาษณ์งานในบริษัท IT 
"""

speech_rate = 200  # ความเร็วเสียง macOS say

def get_ai_response(user_input):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": CHARACTER_PROMPT},
            {"role": "user", "content": user_input},
        ]
    )
    return response["message"]["content"]

def listen_and_transcribe():
    r = sr.Recognizer()
    r.pause_threshold = 1.5   # รอ 4 วินาทีหลังผู้ใช้หยุดพูด
    r.energy_threshold = 300  # ปรับตามสภาพแวดล้อม

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("🎤 พูดได้เลย...")
            audio = r.listen(source, timeout=None, phrase_time_limit=None)
            text = r.recognize_google(audio, language="th-TH")
            print(f"📝 คุณพูดว่า: {text}")
            return text
    except sr.UnknownValueError:
        print("❌ ฟังไม่รู้เรื่องครับ")
    except sr.RequestError as e:
        print(f"❌ ไม่สามารถเชื่อมต่อบริการแปลงเสียง: {e}")
    except Exception as e:
        print(f"❌ เกิดปัญหาเกี่ยวกับไมค์: {e}")
    return None

def speak(text):
    subprocess.call(['say', '-v', 'Kanya', '-r', str(speech_rate), text])

if __name__ == "__main__":
    print("🤖 ระบบเริ่มทำงานแล้ว พูดคำสั่ง 'หยุด' เพื่อจบการทำงาน")
    while True:
        user_input = listen_and_transcribe()

        if not user_input:
            continue

        if user_input.lower() in ["หยุด", "พอแล้ว", "exit", "stop"]:
            print("👋 บ๊ายบาย")
            speak("บ๊ายบายครับ")
            break

        response = get_ai_response(user_input)
        print(f"🤖 Luna: {response}")
        speak(response)