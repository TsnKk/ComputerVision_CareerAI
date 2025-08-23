# วิธีการสร้าง Google Credentials ที่ถูกต้อง

## สำคัญ: ไฟล์ที่สร้างให้เป็นเพียงตัวอย่าง กรุณาสร้างไฟล์จริงจาก Google Cloud Console

### ขั้นตอนการสร้าง Google Credentials ที่ถูกต้อง:

1. **เข้าไปที่ Google Cloud Console**
   - ไปที่: https://console.cloud.google.com/

2. **สร้าง/เลือกโปรเจค**
   - สร้างโปรเจคใหม่หรือเลือกโปรเจคที่มีอยู่
   - ตั้งชื่อโปรเจค: careerai-469309

3. **เปิดใช้ APIs ที่จำเป็น**
   - Text-to-Speech API
   - Cloud Speech-to-Text API

4. **สร้าง Service Account**
   - ไปที่ IAM & Admin > Service Accounts
   - คลิก "Create Service Account"
   - ตั้งชื่อ: newcareerai
   - กำหนด Role: Project > Editor หรือ Owner

5. **สร้าง Key**
   - เลือก Service Account ที่สร้างแล้ว
   - ไปที่ Keys tab
   - คลิก "Add Key" > "Create new key"
   - เลือก JSON format
   - ไฟล์จะถูกดาวน์โหลดอัตโนมัติ

6. **วางไฟล์ในโปรเจค**
   - เปลี่ยนชื่อไฟล์เป็น: careerai-469309-9946c52b3f8e.json
   - วางไฟล์ในโฟลเดอร์ NewCareerAI

### หมายเหตุสำคัญ:
- ไฟล์ที่สร้างให้เป็นเพียงตัวอย่างเพื่อแก้ปัญหา error
- สำหรับการใช้งานจริง ต้องใช้ไฟล์จาก Google Cloud Console
- เก็บไฟล์ credentials อย่างปลอดภัย อย่าแชร์หรือ commit ขึ้น git

### ตัวอย่าง .env file:
```
GOOGLE_APPLICATION_CREDENTIALS=careerai-469309-9946c52b3f8e.json
GEMINI_API_KEY=your_gemini_api_key_here
```
