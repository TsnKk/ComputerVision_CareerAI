import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import pyttsx3
import queue
import time

# ตั้งค่า
RATE = 16000       # sample rate
CHUNK = 1024       # ขนาด frame
SILENCE_THRESHOLD = 500  # ปรับตามความดังไมค์
SILENCE_DURATION = 5     # วินาทีที่ถือว่าเงียบ -> หยุดบันทึก

# โหลดโมเดล Whisper
model = whisper.load_model("medium")

# ฟังก์ชัน Text-to-Speech ภาษาไทย
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # เลือกเสียงไทย macOS (ตัวอย่าง: Kanya)
    engine.setProperty('voice', 'com.apple.voice.compact.th-TH.Kanya')
    engine.say(text)
    engine.runAndWait()

# ฟังก์ชันอัดเสียงแล้วหยุดเมื่อเงียบ
def record_voice(filename="recorded.wav"):
    print("🎤 กำลังอัดเสียง... พูดได้เลย")
    q = queue.Queue()
    recording = []

    def callback(indata, frames, time_info, status):
        if status:
            print(status)
        q.put(indata.copy())

    with sd.InputStream(samplerate=RATE, channels=1, callback=callback, blocksize=CHUNK):
        silent_chunks = 0
        while True:
            chunk = q.get()
            recording.append(chunk)
            amplitude = np.max(np.abs(chunk))
            if amplitude < SILENCE_THRESHOLD:
                silent_chunks += 1
            else:
                silent_chunks = 0

            # ถ้าเงียบครบ SILENCE_DURATION
            if silent_chunks * CHUNK / RATE >= SILENCE_DURATION:
                break

    audio = np.concatenate(recording, axis=0)
    audio = np.int16(audio / np.max(np.abs(audio)) * 32767)
    write(filename, RATE, audio)
    print("✅ อัดเสียงเสร็จแล้ว!")

# ฟังก์ชันถอดเสียง
def transcribe_voice(filename="recorded.wav"):
    print("🧠 กำลังถอดเสียง...")
    result = model.transcribe(filename, language="th")
    text = result["text"]
    print("📜 ข้อความที่ได้:", text)
    return text

# ================= MAIN =================
if __name__ == "__main__":
    record_voice()
    text = transcribe_voice()
    print("🔊 AI กำลังพูดซ้ำ...")
    speak(text)
