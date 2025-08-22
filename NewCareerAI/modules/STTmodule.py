"""
STTmodule.py - Speech-to-Text Module with Whisper
ระบบแปลงเสียงเป็นข้อความด้วย OpenAI Whisper
"""
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import queue
import os

# ตั้งค่าระบบ
RATE = 16000
CHUNK = 1024
SILENCE_THRESHOLD = 500
SILENCE_DURATION = 3  # ลดเวลาเงียบเหลือ 3 วินาที
MIN_RECORDING_DURATION = 1  # อัดขั้นต่ำ 1 วินาที

# โหลดโมเดล Whisper แบบ Global (โหลดครั้งเดียว)
print("🧠 กำลังโหลดโมเดล Whisper...")
try:
    whisper_model = whisper.load_model("base")
    print("✅ โหลดโมเดล Whisper สำเร็จ")
except Exception as e:
    print(f"❌ ไม่สามารถโหลดโมเดล Whisper: {e}")
    whisper_model = None


def record_voice(filename="recorded.wav"):
    """
    อัดเสียงจากไมโครโฟนจนกว่าจะเงียบตาม SILENCE_DURATION
    
    Args:
        filename (str): ชื่อไฟล์เสียงที่จะบันทึก
        
    Returns:
        str: path ของไฟล์เสียง หรือ None หากล้มเหลว
    """
    if whisper_model is None:
        print("❌ โมเดล Whisper ไม่พร้อมใช้งาน")
        return None
        
    print("🎤 กำลังอัดเสียง... (พูดได้เลย)")
    print(f"   - จะหยุดอัดเมื่อเงียบ {SILENCE_DURATION} วินาที")
    print(f"   - กด Ctrl+C เพื่อหยุดบังคับ")
    
    recording_queue = queue.Queue()
    recording_data = []
    silent_chunks = 0
    total_chunks = 0

    def callback(indata, frames, time_info, status):
        if status:
            print(f"⚠️ Audio callback status: {status}")
        recording_queue.put(indata.copy())

    try:
        with sd.InputStream(samplerate=RATE, channels=1, callback=callback, blocksize=CHUNK):
            while True:
                chunk_data = recording_queue.get()
                recording_data.append(chunk_data)
                total_chunks += 1
                
                # คำนวณระดับเสียง
                amplitude = np.max(np.abs(chunk_data))
                
                if amplitude < SILENCE_THRESHOLD:
                    silent_chunks += 1
                else:
                    silent_chunks = 0

                # แสดงสถานะทุกๆ 0.5 วินาที (8 chunks)
                if total_chunks % 8 == 0:
                    duration = total_chunks * CHUNK / RATE
                    print(f"⏱️  อัดแล้ว {duration:.1f}s (เสียง: {amplitude:.0f})")

                # ตรวจสอบเงื่อนไขการหยุดอัด
                recording_duration = total_chunks * CHUNK / RATE
                silent_duration = silent_chunks * CHUNK / RATE
                
                # หยุดถ้าเงียบครบเวลาที่กำหนด และอัดมาแล้วขั้นต่ำ
                if (silent_duration >= SILENCE_DURATION and 
                    recording_duration >= MIN_RECORDING_DURATION):
                    break

    except KeyboardInterrupt:
        print("\n⏹️  หยุดการอัดด้วยผู้ใช้")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการอัดเสียง: {e}")
        return None

    if not recording_data:
        print("❌ ไม่มีข้อมูลเสียง")
        return None

    try:
        # รวมข้อมูลเสียงและปรับระดับ
        audio = np.concatenate(recording_data, axis=0)
        
        # Normalize audio
        if np.max(np.abs(audio)) > 0:
            audio = audio / np.max(np.abs(audio))
            audio = np.int16(audio * 32767)
        else:
            print("❌ ไม่พบสัญญาณเสียง")
            return None
        
        # บันทึกไฟล์
        write(filename, RATE, audio)
        duration = len(audio) / RATE
        print(f"✅ อัดเสียงเสร็จ: {filename} ({duration:.1f} วินาที)")
        
        return filename
        
    except Exception as e:
        print(f"❌ ไม่สามารถบันทึกไฟล์เสียง: {e}")
        return None


def transcribe_voice(filename):
    """
    แปลงไฟล์เสียงเป็นข้อความด้วย Whisper
    
    Args:
        filename (str): ชื่อไฟล์เสียงที่จะแปลง
        
    Returns:
        str: ข้อความที่ถอดได้ หรือ None หากล้มเหลว
    """
    if whisper_model is None:
        print("❌ โมเดล Whisper ไม่พร้อมใช้งาน")
        return None
        
    if not os.path.exists(filename):
        print(f"❌ ไม่พบไฟล์เสียง: {filename}")
        return None

    try:
        print("🧠 กำลังถอดเสียงเป็นข้อความ...")
        result = whisper_model.transcribe(filename, language="th")
        text = result["text"].strip()
        
        if text:
            print(f"📜 ข้อความที่ได้: {text}")
            return text
        else:
            print("❌ ไม่สามารถถอดเสียงได้ (เงียบหรือไม่มีเสียงพูด)")
            return ""
            
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการถอดเสียง: {e}")
        return None


def test_microphone():
    """ทดสอบไมโครโฟน"""
    print("🎤 ทดสอบไมโครโฟน...")
    try:
        devices = sd.query_devices()
        print("📱 อุปกรณ์เสียงที่พบ:")
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0:
                print(f"  {i}: {device['name']}")
        
        default_input = sd.default.device[0]
        print(f"🎯 ไมโครโฟนหลัก: {devices[default_input]['name']}")
        return True
        
    except Exception as e:
        print(f"❌ ไม่สามารถเข้าถึงไมโครโฟน: {e}")
        return False


if __name__ == "__main__":
    # ทดสอบโมดูล
    print("=== ทดสอบ STTmodule ===")
    
    if not test_microphone():
        exit(1)
    
    audio_file = record_voice("test_recording.wav")
    if audio_file:
        text = transcribe_voice(audio_file)
        if text:
            print(f"✅ ผลการทดสอบ: {text}")
        else:
            print("❌ ไม่สามารถถอดเสียงได้")
    else:
        print("❌ การอัดเสียงล้มเหลว")
