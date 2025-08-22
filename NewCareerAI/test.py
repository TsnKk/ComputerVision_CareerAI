# test ทดลองระบบ
import os
import google.generativeai as genai
from TTSmodule import create_tts_client, read_questions
from STTmodule import record_voice, transcribe_voice


# ------------------- ตั้งค่า TTS -------------------
json_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "careerai-469309-9946c52b3f8e.json")
if not os.path.exists(json_path):
    print(f"❌ ไม่พบไฟล์ Google Cloud credentials: {json_path}")
    print("กรุณาตั้งค่า environment variable GOOGLE_APPLICATION_CREDENTIALS")
    exit(1)
tts_client = create_tts_client(json_path)


# ------------------- ตั้งค่า Gemini -------------------
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ ไม่พบ GEMINI_API_KEY environment variable")
    print("กรุณาตั้งค่า environment variable GEMINI_API_KEY")
    exit(1)
genai.configure(api_key=api_key)


# ------------------- กรอก JD -------------------
print("กรอก JD (กด Enter ว่างๆ เพื่อจบ):")
lines = []
while True:
    line = input()
    if line.strip() == "":   # ถ้าผู้ใช้กด Enter เปล่าๆ จะหยุด
        break
    lines.append(line)

jd_text = "\n".join(lines)

print("\n===== ข้อความ JD ที่ได้ =====")
print(jd_text)


# ------------------- สร้างคำถาม -------------------
def generate_questions(jd_text):
    """
    ฟังก์ชันนี้เรียก Google Gemini API
    เพื่อสร้างคำถามสัมภาษณ์งานจาก JD
    คืนค่าเป็น list ของ string
    """

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"""
        กรุณาสร้างคำถามสัมภาษณ์งาน 5 ข้อ จาก Job Description ข้างล่างนี้
        ให้คำถามเป็นประโยคชัดเจน ไม่ยาวและไม่สั้นเกินไป และเหมาะสมสำหรับถามผู้สมัคร เป็นภาษาไทย ไม่ต้องมีคำอธิบายเพิ่มเติม ขอแค่เฉพาะคำถามตามจำนวนข้อที่กำหนด

        Job Description:
        {jd_text}
        """

        response = model.generate_content(prompt)

        # แปลงผลลัพธ์เป็น list
        text = response.text.strip()

        # แยกบรรทัด และกรองบรรทัดว่าง
        questions = [line.strip() for line in text.split("\n") if line.strip()]

        return questions
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return []
# -------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------2
all_questions = []  # เก็บคำถามทั้งหมด
while True:
    try:
        action = input(
            "\nต้องการสร้างคำถามต่อหรือไม่? (พิมพ์ 'next' เพื่อสร้าง / 'exit' เพื่อออก): ").strip().lower()
    except EOFError:
        print("ไม่สามารถรับข้อมูลจากผู้ใช้ได้ (EOFError)")
        break

    if action == "next":
        print("\n===== กำลังสร้างคำถามจาก JD ด้วย AI... =====")
        questions = generate_questions(jd_text)
        if not questions:
            print("ไม่สามารถสร้างคำถามได้ กรุณาตรวจสอบ JD หรือ API Key")
        else:
            all_questions.extend(questions)  # เก็บคำถามทั้งหมดเข้า array
            for i, question in enumerate(questions, 1):
                print(f"คำถามที่ {i}: {question}")
        break
    elif action == "exit":
        print("ออกจากโปรแกรม...")
        break
    else:
        print("ไม่ถูกต้อง! กรุณาพิมพ์ 'next' หรือ 'exit'.")


# ------------------- ฟังก์ชันเปิดกล้องอัดเสียงผู้ใช้ -------------------
# อ่านคำถามและจับเสียงผู้ใช้
# เปิดกล้อง (ตอนนี้คอมไม่มีกล้อง)
all_answers = []

for i, question in enumerate(all_questions, 1):
    print(f"\n--- คำถามที่ {i} ---")
    read_questions(tts_client, [question])  # อ่านคำถาม
    audio_file = record_voice()              # อัดเสียงผู้ใช้
    answer = transcribe_voice(audio_file)    # แปลงเสียงเป็นข้อความ
    all_answers.append(answer)

print("\n===== คำตอบทั้งหมด =====")
for i, ans in enumerate(all_answers, 1):
    print(f"{i}. {ans}")
