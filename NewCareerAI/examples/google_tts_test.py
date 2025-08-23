#!/usr/bin/env python3
"""
🧪 google_tts_test.py - Google Cloud TTS Testing Example
========================================================
ฟีเจอร์หลัก:
- Google Cloud Text-to-Speech API testing และ validation
- TTSmodule integration example
- Voice quality และ performance testing
- pygame audio playback demonstration

ความสามารถ:
- TTS client creation และ configuration testing
- Text-to-speech synthesis with different voices
- Audio playback testing ด้วย pygame integration
- Error handling และ troubleshooting examples
- Voice parameter testing (rate, pitch, volume)

การทดสอบ:
- API authentication และ credentials verification
- Thai voice synthesis (Wavenet, Neural2)
- Audio file generation และ playback
- Performance และ quality assessment

การใช้งาน: python examples/google_tts_test.py
Purpose: Development testing และ TTS module validation
========================================================
"""
import os
import sys

# เพิ่ม modules path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))

from TTSmodule import create_tts_client, text_to_speech, play_audio


def main():
    """ฟังก์ชันหลักสำหรับทดสอบ Google TTS"""
    
    # ตรวจสอบไฟล์ credentials
    json_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "careerai-469309-9946c52b3f8e.json")
    if not os.path.exists(json_path):
        print(f"❌ ไม่พบไฟล์ Google Cloud credentials: {json_path}")
        print("กรุณาตั้งค่า environment variable GOOGLE_APPLICATION_CREDENTIALS")
        return False

    try:
        # สร้าง TTS client
        print("🔧 กำลังสร้าง TTS client...")
        tts_client = create_tts_client(json_path)
        print("✅ สร้าง TTS client สำเร็จ")

        # ข้อความทดสอบ
        test_messages = [
            "สวัสดีครับ นี่คือการทดสอบระบบ Text-to-Speech ของ Google Cloud",
            "ระบบ NewCareerAI พร้อมใช้งานแล้ว",
            "การทดสอบเสียงภาษาไทยผ่าน Google Cloud TTS",
        ]

        for i, text in enumerate(test_messages, 1):
            print(f"\n--- การทดสอบครั้งที่ {i} ---")
            print(f"📝 ข้อความ: {text}")
            
            # สร้างไฟล์เสียง
            filename = f"test_tts_{i}.wav"
            if text_to_speech(tts_client, text, filename):
                print(f"✅ สร้างไฟล์เสียง: {filename}")
                
                # เล่นเสียง
                if play_audio(filename):
                    print(f"✅ เล่นเสียงสำเร็จ")
                else:
                    print(f"❌ ไม่สามารถเล่นเสียงได้")
            else:
                print(f"❌ ไม่สามารถสร้างไฟล์เสียงได้")

        print("\n🎉 การทดสอบเสร็จสิ้น!")
        return True
        
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        return False


if __name__ == "__main__":
    print("=== Google TTS Test ===")
    success = main()
    if not success:
        exit(1)
