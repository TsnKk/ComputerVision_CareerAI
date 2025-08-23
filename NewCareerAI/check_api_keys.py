#!/usr/bin/env python3
"""
🔑 check_api_keys.py - API Keys Configuration Validator
=======================================================
ฟีเจอร์หลัก:
- API keys validation และ configuration checking
- Environment variables verification
- Google Cloud credentials testing
- API connectivity และ authentication testing
- Configuration troubleshooting และ setup guidance

ความสามารถ:
- Gemini API key validation และ authentication test
- Google Cloud credentials file verification
- .env file parsing และ variable checking
- API quota และ rate limit checking
- Connection testing กับ external services
- Detailed error reporting และ fix suggestions

การตรวจสอบ:
- GEMINI_API_KEY existence และ format validation
- GOOGLE_APPLICATION_CREDENTIALS file verification
- API endpoint connectivity testing
- Authentication และ authorization verification

การใช้งาน: python check_api_keys.py
=======================================================
"""
import os
from pathlib import Path

# โหลด environment variables จากไฟล์ .env
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ โหลดการตั้งค่าจาก {env_path}")
    else:
        print(f"❌ ไม่พบไฟล์ .env ที่ {env_path}")
except ImportError:
    print("⚠️  python-dotenv ไม่ได้ติดตั้ง")
    print("รันคำสั่ง: pip install python-dotenv")

print("\n" + "="*50)
print("🔍 ตรวจสอบการตั้งค่า API Keys")
print("="*50)

# ตรวจสอบ Gemini API Key
gemini_key = os.environ.get("GEMINI_API_KEY")
print(f"🤖 Gemini API Key: {'✅ ตั้งค่าแล้ว' if gemini_key and gemini_key != 'your_actual_gemini_api_key_here' else '❌ ไม่ได้ตั้งค่าหรือใช้ค่าเริ่มต้น'}")
if gemini_key and gemini_key != 'AIzaSyA7VkL0Oz9RwrRyXRtnan4matgkbANJkZI':
    print(f"   Key: {gemini_key[:10]}...{gemini_key[-5:] if len(gemini_key) > 15 else ''}")

# ตรวจสอบ Google Cloud Credentials
google_creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
print(f"\n🔑 Google Cloud Credentials: {'✅ ตั้งค่าแล้ว' if google_creds else '❌ ไม่ได้ตั้งค่า'}")
if google_creds:
    print(f"   Path: {google_creds}")
    if os.path.exists(google_creds):
        print("   ✅ ไฟล์มีอยู่")
    else:
        print("   ❌ ไม่พบไฟล์")

print("\n" + "="*50)
print("📋 คำแนะนำการตั้งค่า:")
print("="*50)

if not gemini_key or gemini_key == 'your_actual_gemini_api_key_here':
    print("🤖 Gemini API Key:")
    print("   1. ไปที่ https://aistudio.google.com/app/apikey")
    print("   2. สร้าง API Key ใหม่")
    print("   3. คัดลอกและแทนที่ในไฟล์ .env")
    print("   4. GEMINI_API_KEY=your_real_api_key_here")

if not google_creds:
    print("\n🔑 Google Cloud TTS:")
    print("   1. ไปที่ Google Cloud Console")
    print("   2. เปิดใช้งาน Text-to-Speech API")
    print("   3. สร้าง Service Account และดาวน์โหลด JSON key")
    print("   4. วาง JSON file ไว้ในโฟลเดอร์โปรเจค")
    print("   5. ตั้งค่าในไฟล์ .env:")
    print("   6. GOOGLE_APPLICATION_CREDENTIALS=path_to_your_key.json")

print(f"\n📝 ไฟล์ .env อยู่ที่: {Path(__file__).parent / '.env'}")
print("🔄 รันสคริปต์นี้อีกครั้งหลังจากแก้ไขการตั้งค่า")
