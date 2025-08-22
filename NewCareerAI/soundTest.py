from google.cloud import texttospeech
from playsound import playsound
import os

# สร้าง client จากไฟล์ JSON ของ Service Account
json_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "careerai-469309-9946c52b3f8e.json")
if not os.path.exists(json_path):
    print(f"❌ ไม่พบไฟล์ Google Cloud credentials: {json_path}")
    print("กรุณาตั้งค่า environment variable GOOGLE_APPLICATION_CREDENTIALS")
    exit(1)

tts_client = texttospeech.TextToSpeechClient.from_service_account_file(json_path)

# ข้อความตัวอย่าง
text_input = texttospeech.SynthesisInput(
    text="สวัสดีครับ นี่คือการทดสอบระบบ Text-to-Speech ของ Google Cloud")

# เลือกเสียงและภาษาที่ต้องการ
voice = texttospeech.VoiceSelectionParams(
    language_code="th-TH",
    name="th-TH-Chirp3-HD-Erinome"  # ตัวอย่าง Premium voice
)

# กำหนดรูปแบบไฟล์เสียง
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# เรียก TTS
response = tts_client.synthesize_speech(
    input=text_input,
    voice=voice,
    audio_config=audio_config
)

# เซฟไฟล์เสียง
output_file = "test_tts.mp3"
with open(output_file, "wb") as out:
    out.write(response.audio_content)
print(f"สร้างไฟล์เสียงเสร็จ: {output_file}")

# เล่นเสียง
playsound(output_file)
