from tts_module import TextToSpeech
from stt_module import SpeechToText
from ai_module import AIProcessor
from memory import Memory

def main():
    tts = TextToSpeech()
    stt = SpeechToText()
    ai = AIProcessor(model="llama3")
    memory = Memory()

    print("🤖 ระบบเริ่มทำงานแล้ว พูดคำสั่ง 'หยุด' เพื่อจบการทำงาน")

    while True:
        user_text = stt.listen()
        if not user_text:
            continue

        if "หยุด" in user_text:
            tts.speak("ระบบปิดการทำงานแล้วค่ะ")
            break

        response = ai.ask(user_text)
        tts.speak(response)

        memory.save(user_text, response)

if __name__ == "__main__":
    main()