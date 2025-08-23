# stt_whisper_record.py
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import whisper

SAMPLE_RATE = 16000
DURATION_SEC = 5  # ปรับระยะเวลาที่อัด

def record_to_wav(path, seconds=DURATION_SEC, sr=SAMPLE_RATE):
    print(f"🎙️ กำลังอัดเสียง {seconds} วินาที... พูดได้เลย")
    audio = sd.rec(int(seconds * sr), samplerate=sr, channels=1, dtype='float32')
    sd.wait()
    # แปลง float32 -> int16 ก่อนบันทึก
    audio_int16 = (audio * 32767).astype(np.int16)
    write(path, sr, audio_int16)
    print(f"✅ บันทึกไฟล์ที่: {path}")

def transcribe_whisper(wav_path, model_name="large"):
    # model: tiny/base/small/medium/large  (ตัวใหญ่แม่นกว่าแต่ช้ากว่า)
    print("🧠 โหลดโมเดล Whisper:", model_name)
    model = whisper.load_model(model_name)
    # language='th' จะช่วยชี้นำให้จับไทยดีขึ้น (ปล่อย None ให้โมเดลเดาเองได้เช่นกัน)
    result = model.transcribe(wav_path, language='th')
    return result.get("text", "").strip()

if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = tmp.name
    record_to_wav(wav_path)
    text = transcribe_whisper(wav_path)
    print("📝 คำถอดเสียง:", text)
