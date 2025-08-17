# test ทดลองระบบ
import os
import google.generativeai as genai

# ตั้ง GEMINI API Key
os.environ["API_KEY"] = "AIzaSyARJ3Uwv43vqefMpzqyFofVd3GXVyQxA3I"
genai.configure(api_key=os.environ["API_KEY"])

print("กรอก JD (กด Enter ว่างๆ เพื่อจบ):")
# ---------------------------------------------------------------------------------------------------------------1
lines = []
while True:
    line = input()
    if line.strip() == "":   # ถ้าผู้ใช้กด Enter เปล่าๆ จะหยุด
        break
    lines.append(line)

jd_text = "\n".join(lines)

print("\n===== ข้อความ JD ที่ได้ =====")
print(jd_text)
# ---------------------------------------------------------------------------------------------------------------1


def generate_questions(jd_text):
    """
    ฟังก์ชันนี้เรียก Google Gemini API
    เพื่อสร้างคำถามสัมภาษณ์งานจาก JD
    คืนค่าเป็น list ของ string
    """

# -------------------------------------------------------------------------
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"""
        กรุณาสร้างคำถามสัมภาษณ์งาน 5 ข้อ จาก Job Description ข้างล่างนี้
        ให้คำถามเป็นประโยคสั้น ชัดเจน และเหมาะสมสำหรับถามผู้สมัคร เป็นภาษาไทย ไม่ต้องมีคำอธิบายเพิ่มเติม ขอแค่เฉพาะคำถามตามจำนวนข้อที่กำหนด

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
# ---------------------------------------------------------------------------------------------------------------3
