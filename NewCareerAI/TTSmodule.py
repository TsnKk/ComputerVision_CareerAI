from google.cloud import texttospeech
from playsound import playsound
import os


def create_tts_client(json_path):
    """
    สร้าง Google Cloud TTS client
    json_path: path ของ Service Account Key
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"ไม่พบไฟล์ key: {json_path}")
    return texttospeech.TextToSpeechClient.from_service_account_file(json_path)


def text_to_speech(tts_client, text, filename="output.mp3"):
    """
    แปลงข้อความเป็นเสียง mp3
    tts_client: TTS client
    text: ข้อความ
    filename: ชื่อไฟล์ mp3
    """
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="th-TH",
        name="th-TH-Chirp3-HD-Erinome"  # เลือกโมเดลเสียง Premium
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # บันทึกไฟล์ mp3
    with open(filename, "wb") as f:
        f.write(response.audio_content)


def play_audio(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"ไม่พบไฟล์เสียง: {filename}")
    playsound(filename)


def read_questions(tts_client, questions_array, prefix="question"):
    """
    questions_array: list ของคำถาม
    prefix: ชื่อไฟล์ mp3 ที่จะบันทึก (question_1.mp3, question_2.mp3...)
    """
    for i, q in enumerate(questions_array, 1):
        filename = f"{prefix}_{i}.mp3"
        print(f"กำลังสร้างเสียงสำหรับคำถามที่ {i}...")
        text_to_speech(tts_client, q, filename)
        play_audio(filename)
