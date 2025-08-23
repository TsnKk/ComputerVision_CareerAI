#!/usr/bin/env python3
"""
💼 interview_system.py - Core Interview Processing Engine
==========================================================
ฟีเจอร์หลัก:
- AI-powered interview question generation ด้วย Google Gemini
- Integration ระหว่าง TTS และ STT modules
- Complete interview workflow management
- Job description analysis และการสร้างคำถามที่เหมาะสม
- Interview session management และ tracking

ความสามารถ:
- Generate contextual interview questions
- Process job descriptions และสร้างคำถามตาม requirements
- Manage interview flow และ user responses
- Integration กับ voice recording และ playback systems
- Handle multiple interview rounds และ follow-up questions

ฟีเจอร์ AI:
- Google Generative AI (Gemini) สำหรับสร้างคำถาม
- Context-aware question generation
- Job-specific interview scenarios
- Intelligent follow-up question suggestions

การใช้งาน: python -m core.interview_system
==========================================================
"""
import os
import sys
import google.generativeai as genai

# เพิ่ม modules path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))

from TTSmodule import create_tts_client, read_questions
from STTmodule import record_voice, transcribe_voice


def main():
    """ฟังก์ชันหลักของระบบสัมภาษณ์งาน"""
    
    # ------------------- ตั้งค่า TTS -------------------
    json_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "careerai-469309-9946c52b3f8e.json")
    if not os.path.exists(json_path):
        print(f"❌ ไม่พบไฟล์ Google Cloud credentials: {json_path}")
        print("กรุณาตั้งค่า environment variable GOOGLE_APPLICATION_CREDENTIALS")
        return False
    
    try:
        tts_client = create_tts_client(json_path)
    except Exception as e:
        print(f"❌ ไม่สามารถสร้าง TTS client: {e}")
        return False

    # ------------------- ตั้งค่า Gemini -------------------
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ ไม่พบ GEMINI_API_KEY environment variable")
        print("กรุณาตั้งค่า environment variable GEMINI_API_KEY")
        return False
    
    genai.configure(api_key=api_key)

    # ------------------- กรอก JD -------------------
    print("=== NewCareerAI - ระบบสัมภาษณ์งานขั้นสูง ===")
    print("กรอก Job Description (กด Enter ว่างๆ เพื่อจบ):")
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        except KeyboardInterrupt:
            print("\n❌ ยกเลิกการทำงาน")
            return False
        except EOFError:
            break

    jd_text = "\n".join(lines)
    
    if not jd_text.strip():
        print("❌ ไม่พบ Job Description")
        return False

    print(f"\n{'='*50}")
    print("📋 Job Description ที่ได้:")
    print(f"{'='*50}")
    print(jd_text)
    print(f"{'='*50}")

    # ------------------- สร้างคำถาม -------------------
    questions = generate_questions(jd_text)
    if not questions:
        print("❌ ไม่สามารถสร้างคำถามได้")
        return False

    print(f"\n🤖 สร้างคำถาม {len(questions)} ข้อ สำเร็จ:")
    for i, question in enumerate(questions, 1):
        print(f"  {i}. {question}")

    # ยืนยันการเริ่มสัมภาษณ์
    while True:
        try:
            confirm = input("\n🎯 พร้อมเริ่มการสัมภาษณ์หรือไม่? (y/n): ").strip().lower()
            if confirm in ['y', 'yes', 'ใช่']:
                break
            elif confirm in ['n', 'no', 'ไม่']:
                print("❌ ยกเลิกการสัมภาษณ์")
                return False
        except KeyboardInterrupt:
            print("\n❌ ยกเลิกการทำงาน")
            return False

    # ------------------- เริ่มสัมภาษณ์ -------------------
    print(f"\n{'='*50}")
    print("🎤 เริ่มการสัมภาษณ์งาน")
    print("{'='*50}")
    
    all_answers = []
    
    for i, question in enumerate(questions, 1):
        print(f"\n--- คำถามที่ {i}/{len(questions)} ---")
        print(f"❓ {question}")
        
        try:
            # อ่านคำถาม
            read_questions(tts_client, [question], prefix=f"q{i}")
            
            # อัดเสียงคำตอบ
            audio_file = record_voice(f"answer_{i}.wav")
            
            # ถอดเสียง
            answer = transcribe_voice(audio_file)
            all_answers.append(answer)
            
            print(f"✅ บันทึกคำตอบที่ {i} เรียบร้อย")
            
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในคำถามที่ {i}: {e}")
            all_answers.append("(ไม่สามารถบันทึกคำตอบได้)")

    # ------------------- แสดงผลสรุป -------------------
    print(f"\n{'='*60}")
    print("📊 สรุปผลการสัมภาษณ์")
    print(f"{'='*60}")
    
    for i, (question, answer) in enumerate(zip(questions, all_answers), 1):
        print(f"\n🔹 คำถามที่ {i}:")
        print(f"   {question}")
        print(f"💬 คำตอบ:")
        print(f"   {answer}")
        print("-" * 50)
    
    print("✅ สิ้นสุดการสัมภาษณ์")
    return True


def generate_questions(jd_text):
    """
    สร้างคำถามสัมภาษณ์งานจาก JD ด้วย Gemini AI
    
    Args:
        jd_text (str): Job Description
        
    Returns:
        list: รายการคำถามสัมภาษณ์
    """
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"""
        กรุณาสร้างคำถามสัมภาษณ์งาน 5 ข้อ จาก Job Description ข้างล่างนี้
        ให้คำถามเป็นประโยคชัดเจน ไม่ยาวและไม่สั้นเกินไป และเหมาะสมสำหรับถามผู้สมัคร 
        เป็นภาษาไทย ไม่ต้องมีคำอธิบายเพิ่มเติม ขอแค่เฉพาะคำถามตามจำนวนข้อที่กำหนด
        แต่ละคำถามขึ้นบรรทัดใหม่ ไม่ต้องใส่เลขข้อ

        Job Description:
        {jd_text}
        """

        response = model.generate_content(prompt)
        text = response.text.strip()

        # แยกบรรทัดและกรองบรรทัดว่าง
        questions = []
        for line in text.split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("**"):
                # เอาเลขข้อออก (ถ้ามี)
                import re
                line = re.sub(r'^\d+[\.\)]\s*', '', line)
                questions.append(line)

        return questions[:5]  # จำกัดไม่เกิน 5 ข้อ
        
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการสร้างคำถาม: {e}")
        return []


if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ การทำงานไม่สำเร็จ")
        exit(1)
    else:
        print("\n✅ ระบบทำงานเสร็จสิ้น")
