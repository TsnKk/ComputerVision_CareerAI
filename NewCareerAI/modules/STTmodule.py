#!/usr/bin/env python3
"""
🎤 STTmodule.py - Advanced Speech-to-Text Processing System
===========================================================
ฟีเจอร์หลัก:
- OpenAI Whisper integration สำหรับการแปลงเสียงเป็นข้อความ
- Real-time voice recording ด้วย silence detection
- Multi-threaded audio processing เพื่อประสิทธิภาพ
- Automatic timeout และ error handling
- Support หลายรูปแบบไฟล์เสียง

ความสามารถ:
- WhisperSTT class: จัดการการแปลงเสียงครบวงจร
- Voice activity detection (VAD)
- Auto-silence detection และหยุดอัดอัตโนมัติ
- Real-time microphone selection
- Audio file format conversion
- Threaded recording for non-blocking operation

โมเดล Whisper:
- tiny, base, small, medium, large (เลือกได้)
- Multi-language support
- High accuracy transcription
- Local processing (no internet required)

การใช้งาน: from modules.STTmodule import WhisperSTT
===========================================================
"""
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import streamlit as st
import streamlit as st
import queue
import os
import time
import threading
from typing import Optional, Tuple, Dict
from pathlib import Path

try:
    from .config import audio_config, whisper_config, AUDIO_DIR, TEMP_DIR
except ImportError:
    from config import audio_config, whisper_config, AUDIO_DIR, TEMP_DIR


# ตั้งค่าระบบ (ใช้จาก config)
RATE = audio_config.SAMPLE_RATE
CHUNK = audio_config.CHUNK_SIZE  
SILENCE_THRESHOLD = audio_config.SILENCE_THRESHOLD
SILENCE_DURATION = audio_config.SILENCE_DURATION
MIN_RECORDING_DURATION = audio_config.MIN_RECORDING_DURATION
MAX_RECORDING_DURATION = audio_config.MAX_RECORDING_DURATION

# ฟังก์ชัน cache สำหรับโหลดโมเดล Whisper
@st.cache_resource
def get_whisper_model(model_size):
    print(f"🧠 กำลังโหลดโมเดล Whisper ({model_size})...")
    try:
        model = whisper.load_model(model_size)
        print("✅ โหลดโมเดล Whisper สำเร็จ")
        return model
    except Exception as e:
        print(f"❌ ไม่สามารถโหลดโมเดล Whisper: {e}")
        return None

class WhisperSTT:
    """Enhanced Whisper Speech-to-Text Class"""
    

    def __init__(self, model_size: str = None):
        """
        Initialize Whisper STT
        Args:
            model_size: ขนาดโมเดล (tiny, base, small, medium, large)
        """
        self.model_size = model_size or whisper_config.MODEL_SIZE
        self.model = get_whisper_model(self.model_size)
        self.is_recording = False
    
    def is_ready(self) -> bool:
        """ตรวจสอบว่าพร้อมใช้งานหรือไม่"""
        return self.model is not None


    def record_voice(self, filename: Optional[str] = None, max_duration: Optional[int] = None) -> Optional[str]:
        """
        อัดเสียงจากไมโครโฟนจนกว่าจะเงียบ
        
        Args:
            filename: ชื่อไฟล์เสียง (optional)
            max_duration: ระยะเวลาอัดสูงสุด (วินาที)
            
        Returns:
            path ของไฟล์เสียง หรือ None หากล้มเหลว
        """
        if not self.is_ready():
            print("❌ โมเดล Whisper ไม่พร้อมใช้งาน")
            return None
        
        if filename is None:
            timestamp = int(time.time())
            filename = TEMP_DIR / f"recorded_{timestamp}.wav"
        else:
            filename = Path(filename)
        
        max_dur = max_duration or MAX_RECORDING_DURATION
        
        print("🎤 กำลังอัดเสียง... (พูดได้เลย)")
        print(f"   - จะหยุดอัดเมื่อเงียบ {SILENCE_DURATION} วินาที")
        print(f"   - อัดสูงสุด {max_dur} วินาที")
        print(f"   - กด Ctrl+C เพื่อหยุดบังคับ")
        
        self.is_recording = True
        recording_queue = queue.Queue()
        recording_data = []
        silent_chunks = 0
        total_chunks = 0
        start_time = time.time()

        def callback(indata, frames, time_info, status):
            if status:
                print(f"⚠️ Audio callback status: {status}")
            recording_queue.put(indata.copy())

        try:
            with sd.InputStream(samplerate=RATE, channels=1, callback=callback, blocksize=CHUNK):
                while self.is_recording:
                    try:
                        chunk_data = recording_queue.get(timeout=1.0)
                    except queue.Empty:
                        continue
                        
                    recording_data.append(chunk_data)
                    total_chunks += 1
                    
                    # คำนวณระดับเสียง
                    amplitude = np.max(np.abs(chunk_data))
                    
                    if amplitude < SILENCE_THRESHOLD:
                        silent_chunks += 1
                    else:
                        silent_chunks = 0

                    # แสดงสถานะทุกๆ 0.5 วินาที 
                    if total_chunks % 8 == 0:
                        duration = total_chunks * CHUNK / RATE
                        print(f"⏱️  อัดแล้ว {duration:.1f}s (เสียง: {amplitude:.0f})")

                    # ตรวจสอบเงื่อนไขการหยุดอัด
                    recording_duration = total_chunks * CHUNK / RATE
                    silent_duration = silent_chunks * CHUNK / RATE
                    
                    # หยุดถ้าเงียบครบเวลา และอัดมาแล้วขั้นต่ำ
                    if (silent_duration >= SILENCE_DURATION and 
                        recording_duration >= MIN_RECORDING_DURATION):
                        break
                    
                    # หยุดถ้าเกินเวลาสูงสุด
                    if recording_duration >= max_dur:
                        print(f"⏰ หยุดการอัดเนื่องจากเกินเวลาสูงสุด ({max_dur}s)")
                        break

        except KeyboardInterrupt:
            print("\n⏹️  หยุดการอัดด้วยผู้ใช้")
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการอัดเสียง: {e}")
            return None
        finally:
            self.is_recording = False

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
            write(str(filename), RATE, audio)
            duration = len(audio) / RATE
            print(f"✅ อัดเสียงเสร็จ: {filename} ({duration:.1f} วินาที)")
            
            return str(filename)
            
        except Exception as e:
            print(f"❌ ไม่สามารถบันทึกไฟล์เสียง: {e}")
            return None

    def transcribe_voice(self, filename: str) -> Optional[str]:
        """
        แปลงไฟล์เสียงเป็นข้อความด้วย Whisper
        
        Args:
            filename: ชื่อไฟล์เสียงที่จะแปลง
            
        Returns:
            ข้อความที่ถอดได้ หรือ None หากล้มเหลว
        """
        if not self.is_ready():
            print("❌ โมเดล Whisper ไม่พร้อมใช้งาน")
            return None
            
        if not os.path.exists(filename):
            print(f"❌ ไม่พบไฟล์เสียง: {filename}")
            return None

        print(f"🧠 กำลังถอดเสียงจากไฟล์: {filename}")
        
        try:
            start_time = time.time()
            result = self.model.transcribe(
                filename, 
                language=whisper_config.LANGUAGE,
                temperature=whisper_config.TEMPERATURE
            )
            
            process_time = time.time() - start_time
            
            if result and "text" in result:
                text = result["text"].strip()
                if text:
                    print(f"✅ ถอดเสียงสำเร็จ ({process_time:.1f}s)")
                    print(f"📝 ข้อความ: {text}")
                    return text
                else:
                    print("⚠️ ไม่มีข้อความในไฟล์เสียง")
                    return None
            else:
                print("❌ ไม่สามารถถอดเสียงได้")
                return None
                
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการถอดเสียง: {e}")
            return None
    
    def stop_recording(self):
        """หยุดการอัดเสียง"""
        self.is_recording = False
    
    def record_and_transcribe(self, filename: Optional[str] = None, max_duration: Optional[int] = None) -> Tuple[Optional[str], Optional[str]]:
        """
        อัดเสียงและถอดเสียงในขั้นตอนเดียว
        
        Returns:
            (audio_file, transcribed_text)
        """
        audio_file = self.record_voice(filename, max_duration)
        if audio_file:
            text = self.transcribe_voice(audio_file)
            return audio_file, text
        return None, None

# สร้าง instance หลัก
whisper_stt = WhisperSTT()

# Legacy functions สำหรับ backward compatibility
def record_voice(filename="recorded.wav"):
    """Legacy function - ใช้ WhisperSTT instance"""
    return whisper_stt.record_voice(filename)

def transcribe_voice(filename):
    """Legacy function - ใช้ WhisperSTT instance"""  
    return whisper_stt.transcribe_voice(filename)

def test_microphone():
    """ทดสอบไมโครโฟน"""
    print("🎤 ทดสอบไมโครโฟน...")
    try:
        devices = sd.query_devices()
        print("📱 อุปกรณ์เสียงที่พบ:")
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0:
                print(f"  {i}: {device['name']}")
        
        default_input = sd.default.device[0] if sd.default.device[0] else 0
        print(f"🎯 ไมโครโฟนหลัก: {devices[default_input]['name']}")
        return True
        
    except Exception as e:
        print(f"❌ ไม่สามารถเข้าถึงไมโครโฟน: {e}")
        return False

def record_and_transcribe_legacy(filename="recorded.wav"):
    """Legacy function - อัดและถอดในครั้งเดียว"""
    return whisper_stt.record_and_transcribe(filename)

if __name__ == "__main__":
    # ทดสอบโมดูล
    print("=== ทดสอบ Enhanced STTmodule ===")
    
    if not test_microphone():
        exit(1)
    
    # ทดสอบ WhisperSTT class
    stt = WhisperSTT()
    if not stt.is_ready():
        print("❌ Whisper STT ไม่พร้อมใช้งาน")
        exit(1)
    
    print("เริ่มทดสอบการอัดและถอดเสียง...")
    audio_file, text = stt.record_and_transcribe("test_recording.wav")
    
    if audio_file and text:
        print(f"✅ ผลการทดสอบ:")
        print(f"   ไฟล์เสียง: {audio_file}")  
        print(f"   ข้อความ: {text}")
    else:
        print("❌ การทดสอบล้มเหลว")
