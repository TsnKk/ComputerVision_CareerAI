"""
config.py - Configuration Settings for NewCareerAI
ไฟล์ตั้งค่าสำหรับระบบ NewCareerAI
"""
import os

# === API Configuration ===
GOOGLE_CREDENTIALS_PATH = os.environ.get(
    "GOOGLE_APPLICATION_CREDENTIALS", 
    "careerai-469309-9946c52b3f8e.json"
)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# === Audio Configuration ===
AUDIO_CONFIG = {
    "sample_rate": 16000,
    "chunk_size": 1024,
    "silence_threshold": 500,
    "silence_duration": 3,  # วินาทีที่ถือว่าเงียบ
    "min_recording_duration": 1  # อัดขั้นต่ำ
}

# === TTS Configuration ===
TTS_CONFIG = {
    "language_code": "th-TH",
    "voice_name": "th-TH-Chirp3-HD-Erinome",  # เสียง Premium
    "audio_encoding": "LINEAR16",
    "sample_rate": 16000
}

# === Whisper Configuration ===
WHISPER_CONFIG = {
    "model_size": "base",  # tiny, base, small, medium, large
    "language": "th"
}

# === Interview Configuration ===
INTERVIEW_CONFIG = {
    "max_questions": 5,
    "question_timeout": 30,  # timeout สำหรับการตอบคำถาม (วินาที)
    "gemini_model": "gemini-2.0-flash"
}

# === File Paths ===
AUDIO_DIR = "audio_files"
TEMP_DIR = "temp"

# สร้างโฟลเดอร์หากไม่มี
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# === Validation Functions ===
def validate_config():
    """ตรวจสอบการตั้งค่า"""
    errors = []
    
    # ตรวจสอบ Google Credentials
    if not os.path.exists(GOOGLE_CREDENTIALS_PATH):
        errors.append(f"ไม่พบไฟล์ Google Credentials: {GOOGLE_CREDENTIALS_PATH}")
    
    # ตรวจสอบ Gemini API Key
    if not GEMINI_API_KEY:
        errors.append("ไม่พบ GEMINI_API_KEY environment variable")
    
    return errors

def print_config_status():
    """แสดงสถานะการตั้งค่า"""
    print("=== การตั้งค่าระบบ NewCareerAI ===")
    print(f"🔑 Google Credentials: {GOOGLE_CREDENTIALS_PATH}")
    print(f"   {'✅ พบไฟล์' if os.path.exists(GOOGLE_CREDENTIALS_PATH) else '❌ ไม่พบไฟล์'}")
    print(f"🤖 Gemini API Key: {'✅ ตั้งค่าแล้ว' if GEMINI_API_KEY else '❌ ไม่ได้ตั้งค่า'}")
    print(f"🎤 Audio Sample Rate: {AUDIO_CONFIG['sample_rate']} Hz")
    print(f"🔊 TTS Voice: {TTS_CONFIG['voice_name']}")
    print(f"🧠 Whisper Model: {WHISPER_CONFIG['model_size']}")
    print(f"❓ Max Questions: {INTERVIEW_CONFIG['max_questions']}")
    print("=" * 40)

if __name__ == "__main__":
    print_config_status()
    errors = validate_config()
    if errors:
        print("❌ พบปัญหาการตั้งค่า:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ การตั้งค่าถูกต้องทั้งหมด")
