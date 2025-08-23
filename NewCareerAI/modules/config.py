#!/usr/bin/env python3
"""
⚙️ config.py - Configuration Management System
===============================================
ฟีเจอร์หลัก:
- Centralized configuration management
- Environment variables handling (.env files)
- API keys and credentials management
- Audio recording and playback settings
- AI model configuration (Whisper, TTS, Gemini)
- File path and directory management

ความสามารถ:
- APIConfig: จัดการ Gemini API และ Google Cloud credentials
- AudioConfig: ตั้งค่าการอัดและเล่นเสียง
- TTSConfig: กำหนดเสียงและความเร็วของ TTS
- WhisperConfig: เลือกโมเดล STT และการตั้งค่า
- InterviewConfig: จำนวนคำถามและรูปแบบการสัมภาษณ์

คลาสหลัก:
- APIConfig, AudioConfig, TTSConfig, WhisperConfig, InterviewConfig
- ฟังก์ชัน get_* สำหรับดึงค่าการตั้งค่าแต่ละประเภท

การใช้งาน: from modules.config import get_api_config
===============================================
"""
import os
import json
from pathlib import Path
from typing import Dict, List, Optional

# โหลด environment variables จากไฟล์ .env
try:
    from dotenv import load_dotenv
    # หา path ของไฟล์ .env
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ โหลดการตั้งค่าจาก {env_path}")
    else:
        print(f"⚠️  ไม่พบไฟล์ .env ที่ {env_path}")
except ImportError:
    print("⚠️  python-dotenv ไม่ได้ติดตั้ง กำลังใช้ system environment variables")

# === Project Paths ===
PROJECT_ROOT = Path(__file__).parent.parent
AUDIO_DIR = PROJECT_ROOT / "audio_files"
TEMP_DIR = PROJECT_ROOT / "temp"
DATA_DIR = PROJECT_ROOT / "data"

# สร้างโฟลเดอร์หากไม่มี
for dir_path in [AUDIO_DIR, TEMP_DIR, DATA_DIR]:
    dir_path.mkdir(exist_ok=True)

# === API Configuration ===
class APIConfig:
    """API การตั้งค่า"""
    
    @property
    def google_credentials_path(self) -> str:
        """Path ไฟล์ Google Service Account"""
        env_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if env_path and os.path.exists(env_path):
            return env_path
        
        # ลองหาในโฟลเดอร์โปรเจ็กต์
        local_files = [
            "careerai-469309-9946c52b3f8e.json",
            "service-account.json",
            "google-credentials.json"
        ]
        
        for file_name in local_files:
            file_path = PROJECT_ROOT / file_name
            if file_path.exists():
                return str(file_path)
        
        return "careerai-469309-9946c52b3f8e.json"
    
    @property
    def gemini_api_key(self) -> Optional[str]:
        """Gemini API Key"""
        return os.environ.get("GEMINI_API_KEY")
    
    @property
    def is_valid(self) -> bool:
        """ตรวจสอบว่า API Config พร้อมใช้งาน"""
        return (os.path.exists(self.google_credentials_path) and 
                self.gemini_api_key is not None)

# สร้าง instance
api_config = APIConfig()

# เก็บ legacy variables สำหรับ backward compatibility
GOOGLE_CREDENTIALS_PATH = api_config.google_credentials_path
GEMINI_API_KEY = api_config.gemini_api_key

# === Enhanced Configuration Classes ===
class AudioConfig:
    """การตั้งค่าเสียง"""
    SAMPLE_RATE = 16000
    CHUNK_SIZE = 1024
    SILENCE_THRESHOLD = 500
    SILENCE_DURATION = 3  # วินาที
    MIN_RECORDING_DURATION = 1  # วินาที
    MAX_RECORDING_DURATION = 30  # วินาที
    
    @classmethod
    def to_dict(cls) -> Dict:
        return {
            "sample_rate": cls.SAMPLE_RATE,
            "chunk_size": cls.CHUNK_SIZE,
            "silence_threshold": cls.SILENCE_THRESHOLD,
            "silence_duration": cls.SILENCE_DURATION,
            "min_recording_duration": cls.MIN_RECORDING_DURATION,
            "max_recording_duration": cls.MAX_RECORDING_DURATION,
        }

class TTSConfig:
    """การตั้งค่า Text-to-Speech"""
    LANGUAGE_CODE = "th-TH"
    VOICE_NAME = "th-TH-Wavenet-C"  # เสียงผู้หญิงไทย
    AUDIO_ENCODING = "LINEAR16"
    SAMPLE_RATE = 16000
    SPEAKING_RATE = 1.0  # ความเร็วการพูด
    PITCH = 0.0  # ระดับเสียง
    VOLUME_GAIN_DB = 0.0  # ระดับเสียง
    
    # เสียงทางเลือก
    VOICE_OPTIONS = {
        "female": "th-TH-Wavenet-C",
        "male": "th-TH-Wavenet-B",
        "premium": "th-TH-Chirp3-HD-Erinome"
    }
    
    @classmethod
    def to_dict(cls) -> Dict:
        return {
            "language_code": cls.LANGUAGE_CODE,
            "voice_name": cls.VOICE_NAME,
            "audio_encoding": cls.AUDIO_ENCODING,
            "sample_rate": cls.SAMPLE_RATE,
            "speaking_rate": cls.SPEAKING_RATE,
            "pitch": cls.PITCH,
            "volume_gain_db": cls.VOLUME_GAIN_DB,
        }

class WhisperConfig:
    """การตั้งค่า Whisper STT"""
    MODEL_SIZE = "base"  # tiny, base, small, medium, large
    LANGUAGE = "th"
    TEMPERATURE = 0.0  # ความสม่ำเสมอในผลลัพธ์
    
    MODEL_OPTIONS = {
        "tiny": "เร็วที่สุด แต่แม่นยำน้อย",
        "base": "สมดุลระหว่างความเร็วและความแม่นยำ", 
        "small": "แม่นยำมากขึ้น ใช้เวลานานขึ้น",
        "medium": "แม่นยำสูง ใช้เวลาค่อนข้างนาน",
        "large": "แม่นยำที่สุด ใช้เวลานานที่สุด"
    }
    
    @classmethod
    def to_dict(cls) -> Dict:
        return {
            "model_size": cls.MODEL_SIZE,
            "language": cls.LANGUAGE,
            "temperature": cls.TEMPERATURE,
        }

class InterviewConfig:
    """การตั้งค่าการสัมภาษณ์"""
    MAX_QUESTIONS = 10  # เพิ่มจาก 5 เป็น 10
    QUESTION_TIMEOUT = 60  # เพิ่มเวลาตอบ
    GEMINI_MODEL = "gemini-2.0-flash"
    
    # ประเภทการสัมภาษณ์
    INTERVIEW_TYPES = {
        "technical": "สัมภาษณ์ด้านเทคนิค",
        "behavioral": "สัมภาษณ์ด้านพฤติกรรม", 
        "mixed": "สัมภาษณ์แบบผสม",
        "custom": "กำหนดเองโดยผู้ใช้"
    }
    
    @classmethod
    def to_dict(cls) -> Dict:
        return {
            "max_questions": cls.MAX_QUESTIONS,
            "question_timeout": cls.QUESTION_TIMEOUT,
            "gemini_model": cls.GEMINI_MODEL,
            "interview_types": cls.INTERVIEW_TYPES,
        }

# สร้าง instances สำหรับใช้งาน
audio_config = AudioConfig()
tts_config = TTSConfig()
whisper_config = WhisperConfig()
interview_config = InterviewConfig()

# Legacy dictionaries สำหรับ backward compatibility
AUDIO_CONFIG = audio_config.to_dict()
TTS_CONFIG = tts_config.to_dict()
WHISPER_CONFIG = whisper_config.to_dict()
INTERVIEW_CONFIG = interview_config.to_dict()

# === Enhanced Validation and Utility Functions ===
def validate_config() -> List[str]:
    """ตรวจสอบการตั้งค่าแบบละเอียด"""
    errors = []
    
    # ตรวจสอบ Google Credentials
    if not os.path.exists(api_config.google_credentials_path):
        errors.append(f"ไม่พบไฟล์ Google Credentials: {api_config.google_credentials_path}")
    
    # ตรวจสอบ Gemini API Key
    if not api_config.gemini_api_key:
        errors.append("ไม่พบ GEMINI_API_KEY environment variable")
    
    # ตรวจสอบโฟลเดอร์ที่จำเป็น
    required_dirs = [AUDIO_DIR, DATA_DIR]
    for dir_path in required_dirs:
        if not dir_path.exists():
            try:
                dir_path.mkdir(exist_ok=True)
                print(f"✅ สร้างโฟลเดอร์: {dir_path}")
            except Exception as e:
                errors.append(f"ไม่สามารถสร้างโฟลเดอร์ {dir_path}: {e}")
    
    return errors

def print_config_status():
    """แสดงสถานะการตั้งค่าแบบละเอียด"""
    print("=" * 50)
    print("🚀 สถานะการตั้งค่าระบบ NewCareerAI")
    print("=" * 50)
    
    # API Settings
    print("📡 API Configuration:")
    print(f"   🔑 Google Credentials: {api_config.google_credentials_path}")
    print(f"      {'✅ พบไฟล์' if os.path.exists(api_config.google_credentials_path) else '❌ ไม่พบไฟล์'}")
    print(f"   🤖 Gemini API Key: {'✅ ตั้งค่าแล้ว' if api_config.gemini_api_key else '❌ ไม่ได้ตั้งค่า'}")
    
    # Audio Settings
    print("\n� Audio Configuration:")
    print(f"   🎤 Sample Rate: {audio_config.SAMPLE_RATE:,} Hz")
    print(f"   ⏱️  Max Recording: {audio_config.MAX_RECORDING_DURATION} วินาที")
    print(f"   🔇 Silence Duration: {audio_config.SILENCE_DURATION} วินาที")
    
    # TTS Settings
    print("\n🔊 Text-to-Speech Configuration:")
    print(f"   🗣️  Voice: {tts_config.VOICE_NAME}")
    print(f"   🌏 Language: {tts_config.LANGUAGE_CODE}")
    print(f"   ⚡ Speaking Rate: {tts_config.SPEAKING_RATE}")
    
    # Whisper Settings
    print("\n🧠 Whisper STT Configuration:")
    print(f"   📊 Model Size: {whisper_config.MODEL_SIZE}")
    print(f"   💬 Language: {whisper_config.LANGUAGE}")
    
    # Interview Settings
    print("\n❓ Interview Configuration:")
    print(f"   📝 Max Questions: {interview_config.MAX_QUESTIONS}")
    print(f"   ⏰ Question Timeout: {interview_config.QUESTION_TIMEOUT} วินาที")
    print(f"   🤖 AI Model: {interview_config.GEMINI_MODEL}")
    
    # Directories
    print("\n📁 Directory Structure:")
    print(f"   📂 Project Root: {PROJECT_ROOT}")
    print(f"   🔊 Audio Files: {AUDIO_DIR}")
    print(f"   💾 Data Files: {DATA_DIR}")
    print(f"   🗂️  Temp Files: {TEMP_DIR}")
    
    print("=" * 50)

def save_config_to_file(file_path: Optional[str] = None):
    """บันทึกการตั้งค่าลงไฟล์ JSON"""
    if file_path is None:
        file_path = DATA_DIR / "config_backup.json"
    
    config_data = {
        "api": {
            "google_credentials_path": api_config.google_credentials_path,
            "gemini_api_key_set": api_config.gemini_api_key is not None
        },
        "audio": audio_config.to_dict(),
        "tts": tts_config.to_dict(),
        "whisper": whisper_config.to_dict(),
        "interview": interview_config.to_dict(),
        "paths": {
            "project_root": str(PROJECT_ROOT),
            "audio_dir": str(AUDIO_DIR),
            "data_dir": str(DATA_DIR),
            "temp_dir": str(TEMP_DIR)
        }
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=2)
        print(f"✅ บันทึกการตั้งค่าที่: {file_path}")
    except Exception as e:
        print(f"❌ ไม่สามารถบันทึกการตั้งค่า: {e}")

def get_system_info() -> Dict:
    """ดึงข้อมูลระบบ"""
    import platform
    import sys
    
    return {
        "platform": platform.platform(),
        "python_version": sys.version,
        "python_executable": sys.executable,
        "current_directory": os.getcwd()
    }

if __name__ == "__main__":
    print_config_status()
    errors = validate_config()
    if errors:
        print("❌ พบปัญหาการตั้งค่า:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ การตั้งค่าถูกต้องทั้งหมด")
