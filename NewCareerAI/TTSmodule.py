from google.cloud import texttospeech
import os
import pygame  # ✅ เพิ่ม


def create_tts_client(json_path):
    """
    สร้าง Google Cloud TTS client
    json_path: path ของ Service Account Key
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"ไม่พบไฟล์ key: {json_path}")
    return texttospeech.TextToSpeechClient.from_service_account_file(json_path)


def text_to_speech(tts_client, text, filename="output.wav"):
    """
    แปลงข้อความเป็นเสียง wav
    tts_client: TTS client
    text: ข้อความ
    filename: ชื่อไฟล์ wav
    """
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="th-TH",
        name="th-TH-Chirp3-HD-Erinome"  # เลือกโมเดลเสียง Premium
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # บันทึกไฟล์ wav
    with open(filename, "wb") as f:
        f.write(response.audio_content)


def play_audio(filename):
    """
    เล่นไฟล์เสียงด้วย pygame
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"ไม่พบไฟล์เสียง: {filename}")

    pygame.mixer.init()         # ✅ เพิ่ม
    pygame.mixer.music.load(filename)  # ✅ โหลดไฟล์
    pygame.mixer.music.play()          # ✅ เล่นไฟล์

    # รอจนกว่าเสียงเล่นเสร็จ
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def read_questions(tts_client, questions_array, prefix="question"):
    for i, q in enumerate(questions_array, 1):
        filename = f"{prefix}_{i}.wav"
        print(f"กำลังสร้างเสียงสำหรับคำถามที่ {i}...")

        # หยุด pygame ก่อนเขียนทับไฟล์
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit()

        text_to_speech(tts_client, q, filename)
        play_audio(filename)
