import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import queue

# ตั้งค่า
RATE = 16000
CHUNK = 1024
SILENCE_THRESHOLD = 500
SILENCE_DURATION = 5  # วินาทีที่ถือว่าเงียบ -> หยุดบันทึก

# โหลดโมเดล Whisper
whisper_model = whisper.load_model("medium")


def record_voice(filename="recorded.wav"):
    """
    อัดเสียงจากไมโครโฟนจนกว่าจะเงียบตาม SILENCE_DURATION
    คืนค่า path ของไฟล์เสียง
    """
    print("🎤 กำลังอัดเสียง... พูดได้เลย")
    q = queue.Queue()
    recording = []

    def callback(indata, frames, time_info, status):
        if status:
            print(status)
        q.put(indata.copy())

    silent_chunks = 0
    with sd.InputStream(samplerate=RATE, channels=1, callback=callback, blocksize=CHUNK):
        while True:
            chunk_data = q.get()
            recording.append(chunk_data)
            amplitude = np.max(np.abs(chunk_data))
            if amplitude < SILENCE_THRESHOLD:
                silent_chunks += 1
            else:
                silent_chunks = 0
            if silent_chunks * CHUNK / RATE >= SILENCE_DURATION:
                break

    audio = np.concatenate(recording, axis=0)
    audio = np.int16(audio / np.max(np.abs(audio)) * 32767)
    write(filename, RATE, audio)
    print("✅ เสร็จสิ้นการอัดเสียง")
    return filename


def transcribe_voice(filename):
    """
    แปลงไฟล์เสียงเป็นข้อความ
    """
    print("🧠 กำลังถอดเสียง...")
    result = whisper_model.transcribe(filename, language="th")
    text = result["text"]
    print("📜 ข้อความที่ได้:", text)
    return text
