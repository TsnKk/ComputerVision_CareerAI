#!/usr/bin/env python3
"""
🔊 TTSmodule.py - Google Cloud Text-to-Speech Engine
=====================================================
ฟีเจอร์หลัก:
- Google Cloud TTS integration สำหรับการแปลงข้อความเป็นเสียง
- Support เสียงภาษาไทยคุณภาพสูง (Wavenet voices)
- Real-time audio synthesis และ playback
- Audio file management และ caching
- Multiple voice profiles และ speech settings

ความสามารถ:
- GoogleTTS class: จัดการการสังเคราะห์เสียงครบวงจร
- Thai voice support (th-TH-Wavenet-C, Neural2 voices)
- Customizable speech rate, pitch, และ volume
- pygame integration สำหรับการเล่นเสียง
- Automatic audio file cleanup
- Threaded audio processing
- Error handling และ fallback mechanisms

เสียงที่รองรับ:
- Standard voices: th-TH-Standard-A
- Wavenet voices: th-TH-Wavenet-A/B/C
- Neural2 voices: th-TH-Neural2-C
- Premium quality synthesis

การใช้งาน: from modules.TTSmodule import GoogleTTS
=====================================================
"""
from google.cloud import texttospeech
import os
import pygame
import time
import io
from pathlib import Path
from typing import Optional, Dict, List, Union
import threading
import queue

try:
    from .config import tts_config, api_config, AUDIO_DIR, TEMP_DIR
except ImportError:
    from config import tts_config, api_config, AUDIO_DIR, TEMP_DIR

class GoogleTTS:
    """Enhanced Google Cloud Text-to-Speech Class"""
    
    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize Google TTS
        
        Args:
            credentials_path: path ของ Service Account Key
        """
        self.credentials_path = credentials_path or api_config.google_credentials_path
        self.client = None
        self.is_ready = False
        self.pygame_initialized = False
        self.current_audio = None
        self._init_client()
        self._init_pygame()
    
    def _init_client(self):
        """เริ่มต้น TTS client"""
        if not os.path.exists(self.credentials_path):
            print(f"❌ ไม่พบไฟล์ Google Credentials: {self.credentials_path}")
            return
        
        try:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credentials_path
            self.client = texttospeech.TextToSpeechClient()
            self.is_ready = True
            print("✅ Google Cloud TTS พร้อมใช้งาน")
        except Exception as e:
            print(f"❌ ไม่สามารถสร้าง TTS client: {e}")
            self.is_ready = False
    
    def _init_pygame(self):
        """เริ่มต้น pygame mixer"""
        try:
            pygame.mixer.init(frequency=tts_config.SAMPLE_RATE, size=-16, channels=1, buffer=2048)
            self.pygame_initialized = True
        except Exception as e:
            print(f"⚠️ pygame mixer ไม่สามารถเริ่มต้นได้: {e}")
            self.pygame_initialized = False


    def get_voice_options(self) -> Dict[str, str]:
        """ดึงรายการเสียงที่พร้อมใช้งาน"""
        return tts_config.VOICE_OPTIONS.copy()
    
    def set_voice(self, voice_type: str = "female"):
        """
        เปลี่ยนเสียงที่ใช้
        
        Args:
            voice_type: ประเภทเสียง (female, male, premium)
        """
        if voice_type in tts_config.VOICE_OPTIONS:
            tts_config.VOICE_NAME = tts_config.VOICE_OPTIONS[voice_type]
            print(f"✅ เปลี่ยนเสียงเป็น: {tts_config.VOICE_NAME}")
        else:
            print(f"❌ ไม่พบประเภทเสียง: {voice_type}")
    
    def text_to_speech(self, text: str, filename: Optional[str] = None, voice_type: Optional[str] = None) -> Optional[str]:
        """
        แปลงข้อความเป็นเสียง wav
        
        Args:
            text: ข้อความที่ต้องการแปลง
            filename: ชื่อไฟล์เสียง (optional)
            voice_type: ประเภทเสียง (optional)
            
        Returns:
            path ของไฟล์เสียง หรือ None หากล้มเหลว
        """
        if not self.is_ready:
            print("❌ Google TTS ไม่พร้อมใช้งาน")
            return None
        
        if not text or not text.strip():
            print("❌ ข้อความว่าง")
            return None
        
        # สร้างชื่อไฟล์ถ้าไม่ได้ระบุ
        if filename is None:
            timestamp = int(time.time())
            filename = TEMP_DIR / f"tts_output_{timestamp}.wav"
        else:
            filename = Path(filename)
        
        # เปลี่ยนเสียงถ้าได้ระบุ
        current_voice = tts_config.VOICE_NAME
        if voice_type and voice_type in tts_config.VOICE_OPTIONS:
            current_voice = tts_config.VOICE_OPTIONS[voice_type]
        
        try:
            print(f"🗣️  กำลังสร้างเสียงจาก: '{text[:50]}{'...' if len(text) > 50 else ''}'")
            
            synthesis_input = texttospeech.SynthesisInput(text=text)
            voice = texttospeech.VoiceSelectionParams(
                language_code=tts_config.LANGUAGE_CODE,
                name=current_voice
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16,
                sample_rate_hertz=tts_config.SAMPLE_RATE,
                speaking_rate=tts_config.SPEAKING_RATE,
                pitch=tts_config.PITCH,
                volume_gain_db=tts_config.VOLUME_GAIN_DB
            )

            start_time = time.time()
            response = self.client.synthesize_speech(
                input=synthesis_input, 
                voice=voice, 
                audio_config=audio_config
            )
            
            # บันทึกไฟล์ wav
            with open(filename, "wb") as f:
                f.write(response.audio_content)
            
            process_time = time.time() - start_time
            print(f"✅ สร้างเสียงสำเร็จ: {filename} ({process_time:.1f}s)")
            return str(filename)
            
        except Exception as e:
            print(f"❌ ไม่สามารถสร้างเสียงได้: {e}")
            return None

    def play_audio(self, filename: str, wait: bool = True) -> bool:
        """
        เล่นไฟล์เสียงด้วย pygame
        
        Args:
            filename: ชื่อไฟล์เสียงที่จะเล่น
            wait: รอจนกว่าเล่นเสร็จ
            
        Returns:
            True หากเล่นสำเร็จ
        """
        if not os.path.exists(filename):
            print(f"❌ ไม่พบไฟล์เสียง: {filename}")
            return False

        if not self.pygame_initialized:
            print("❌ pygame mixer ไม่พร้อมใช้งาน")
            return False

        try:
            # หยุดเสียงก่อนหน้า
            pygame.mixer.music.stop()
            
            # โหลดและเล่นไฟล์
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            
            print(f"🔊 เล่นเสียง: {Path(filename).name}")

            # รอจนกว่าเสียงเล่นเสร็จ
            if wait:
                while pygame.mixer.music.get_busy():
                    pygame.time.wait(100)
                print("✅ เล่นเสียงเสร็จ")
            
            return True
            
        except Exception as e:
            print(f"❌ ไม่สามารถเล่นเสียงได้: {e}")
            return False
    
    def speak(self, text: str, voice_type: Optional[str] = None, save_file: bool = False) -> bool:
        """
        พูดข้อความ (สร้างเสียงและเล่นทันที)
        
        Args:
            text: ข้อความที่จะพูด
            voice_type: ประเภทเสียง
            save_file: บันทึกไฟล์หรือไม่
            
        Returns:
            True หากสำเร็จ
        """
        # สร้างไฟล์เสียง
        if save_file:
            timestamp = int(time.time())
            filename = AUDIO_DIR / f"speech_{timestamp}.wav"
        else:
            filename = TEMP_DIR / f"temp_speech_{int(time.time())}.wav"
        
        audio_file = self.text_to_speech(text, filename, voice_type)
        if audio_file:
            success = self.play_audio(audio_file)
            
            # ลบไฟล์ temp หลังใช้
            if not save_file:
                try:
                    os.remove(audio_file)
                except:
                    pass
            
            return success
        return False
    
    def stop_audio(self):
        """หยุดการเล่นเสียง"""
        if self.pygame_initialized:
            pygame.mixer.music.stop()
    
    def is_playing(self) -> bool:
        """ตรวจสอบว่าเสียงกำลังเล่นอยู่หรือไม่"""
        return pygame.mixer.music.get_busy() if self.pygame_initialized else False

# สร้าง instance หลัก
google_tts = GoogleTTS()

# Legacy functions สำหรับ backward compatibility
def create_tts_client(json_path):
    """Legacy function - สร้าง TTS client"""
    try:
        tts = GoogleTTS(json_path)
        return tts.client if tts.is_ready else None
    except Exception as e:
        print(f"❌ ไม่สามารถสร้าง TTS client: {e}")
        return None

def text_to_speech(tts_client, text, filename="output.wav"):
    """Legacy function - ใช้ GoogleTTS instance"""
    return google_tts.text_to_speech(text, filename) is not None

def play_audio(filename):
    """Legacy function - ใช้ GoogleTTS instance"""
    return google_tts.play_audio(filename)

def speak(text, voice_type=None):
    """Legacy function - พูดข้อความ"""
    return google_tts.speak(text, voice_type)

def read_questions(tts_client, questions_array, prefix="question"):
    """
    อ่านคำถามทั้งหมดด้วยเสียง (Enhanced)
    
    Args:
        tts_client: TTS client object (ignored - ใช้ google_tts)
        questions_array: รายการคำถาม
        prefix: prefix สำหรับชื่อไฟล์
        
    Returns:
        True หากสำเร็จ
    """
    if not google_tts.is_ready:
        print("❌ Google TTS ไม่พร้อมใช้งาน")
        return False
    
    success = True
    
    for i, question in enumerate(questions_array, 1):
        print(f"🔊 คำถามที่ {i}: {question}")
        
        # สร้างและเล่นเสียง
        if not google_tts.speak(question, save_file=True):
            print(f"❌ ไม่สามารถพูดคำถามที่ {i}")
            success = False
            continue
            
        print(f"✅ เล่นคำถามที่ {i} เรียบร้อย")
        
        # หน่วงเวลาก่อนคำถามถัดไป
        time.sleep(0.5)
    
    return success

def cleanup_pygame():
    """ทำความสะอาด pygame mixer"""
    if google_tts.pygame_initialized:
        google_tts.stop_audio()
    try:
        pygame.mixer.quit()
    except:
        pass

if __name__ == "__main__":
    # ทดสอบโมดูล
    print("=== ทดสอบ Enhanced TTSmodule ===")
    
    if not google_tts.is_ready:
        print("❌ Google TTS ไม่พร้อมใช้งาน")
        exit(1)
    
    # ทดสอบการพูด
    test_text = "สวัสดีครับ นี่คือการทดสอบระบบ Text-to-Speech"
    print(f"ทดสอบการพูด: {test_text}")
    
    if google_tts.speak(test_text):
        print("✅ การทดสอบสำเร็จ")
    else:
        print("❌ การทดสอบล้มเหลว")
    
    # ทดสอบเสียงต่างๆ
    print("\nทดสอบเสียงต่างๆ:")
    voices = google_tts.get_voice_options()
    for voice_type, voice_name in voices.items():
        print(f"ทดสอบเสียง {voice_type}: {voice_name}")
        google_tts.speak(f"ทดสอบเสียง {voice_type}", voice_type=voice_type)
        time.sleep(1)
