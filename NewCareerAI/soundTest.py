from google.cloud import texttospeech
from playsound import playsound

# สร้าง client จากไฟล์ JSON ของ Service Account
json_path = "D:\\NewCareerAI\\careerai-469309-9946c52b3f8e.json"
tts_client = texttospeech.TextToSpeechClient.from_service_account_file(
    json_path)

# ข้อความตัวอย่าง
text_input = texttospeech.SynthesisInput(
    text="ไอเหนือเป็นเปโด ไอเกมก็ชอบเด็ก แต่ความจริงไอแซนเป็นคนกัมพุชา แต่มันไม่ยอมรับ")

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
