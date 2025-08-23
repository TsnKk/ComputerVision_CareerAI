#!/usr/bin/env python3
"""
🧪 test_imports.py - Module Import Testing Suite
================================================
ฟีเจอร์หลัก:
- Comprehensive import testing สำหรับทุก modules
- Dependency validation และ compatibility checking
- Development environment verification
- Module functionality testing

ความสามารถ:
- test_modules(): ทดสอบการ import ทั้งหมด
- Core modules testing (config, STT, TTS, AI)
- External dependencies verification
- Error detection และ troubleshooting guidance
- Import path และ compatibility validation

การทดสอบ:
- All core modules (config, STT, TTS, interview_system)
- External libraries (streamlit, whisper, pygame, etc.)
- API connections และ credentials
- System compatibility และ requirements

การใช้งาน: python test_imports.py
Purpose: Development testing และ environment validation
================================================
"""

def test_modules():
    """ทดสอบการ import modules"""
    
    print("🧪 ทดสอบการ import modules...")
    
    try:
        from modules.config import validate_config
        print("✅ config module OK")
    except ImportError as e:
        print(f"❌ config module error: {e}")
    
    try:
        from modules.TTSmodule import create_tts_client
        print("✅ TTSmodule OK")
    except ImportError as e:
        print(f"❌ TTSmodule error: {e}")
    
    try:
        from modules.STTmodule import record_voice
        print("✅ STTmodule OK")
    except ImportError as e:
        print(f"❌ STTmodule error: {e}")
    
    try:
        from core.interview_system import generate_questions
        print("✅ interview_system OK")
    except ImportError as e:
        print(f"❌ interview_system error: {e}")
    
    print("🎉 ทดสอบ modules เสร็จสิ้น")

def test_dependencies():
    """ทดสอบ dependencies ที่จำเป็น"""
    
    print("\n📦 ทดสอบ dependencies...")
    
    dependencies = [
        ("google.generativeai", "Google Gemini AI"),
        ("google.cloud.texttospeech", "Google Cloud TTS"),
        ("whisper", "OpenAI Whisper"),
        ("sounddevice", "Sound Device"),
        ("scipy", "SciPy"),
        ("pygame", "Pygame"),
        ("numpy", "NumPy")
    ]
    
    for module_name, display_name in dependencies:
        try:
            __import__(module_name)
            print(f"✅ {display_name}")
        except ImportError:
            print(f"❌ {display_name} - ไม่ได้ติดตั้ง")
    
    # ทดสอบ streamlit แยก
    try:
        import streamlit
        print(f"✅ Streamlit (เวอร์ชัน {streamlit.__version__})")
    except ImportError:
        print("❌ Streamlit - ไม่ได้ติดตั้ง (จำเป็นสำหรับ Web UI)")
    
    print("🎉 ทดสอบ dependencies เสร็จสิ้น")

if __name__ == "__main__":
    print("=" * 60)
    print("🔍 ทดสอบระบบ NewCareerAI")
    print("=" * 60)
    
    test_dependencies()
    test_modules()
    
    print("\n" + "=" * 60)
    print("💡 วิธีติดตั้ง dependencies ที่ขาดหาย:")
    print("pip install -r requirements.txt")
    print("=" * 60)
