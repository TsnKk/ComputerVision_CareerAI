import subprocess

class TextToSpeech:
    def speak(self, text):
        try:
            subprocess.run(["say", text])  # macOS built-in TTS
        except Exception as e:
            print(f"⚠️ ไม่สามารถพูดข้อความได้: {e}")

    def speak(self, text):
        print(f"🤖 Luna: {text}")
        self.engine.say(text)
        self.engine.runAndWait()