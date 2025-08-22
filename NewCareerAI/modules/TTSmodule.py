"""
TTSmodule.py - Google Cloud Text-to-Speech Module
ระบบแปลงข้อความเป็นเสียงด้วย Google Cloud TTS
"""
from google.cloud import texttospeech
import os
import pygame
import time


def create_tts_client(json_path):
    """
    สร้าง Google Cloud TTS client
    
    Args:
        json_path (str): path ของ Service Account Key
        
    Returns:
        TextToSpeechClient: TTS client object
        
    Raises:
        FileNotFoundError: ถ้าไม่พบไฟล์ key
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"ไม่พบไฟล์ key: {json_path}")
    
    try:
        return texttospeech.TextToSpeechClient.from_service_account_file(json_path)
    except Exception as e:
        raise Exception(f"ไม่สามารถสร้าง TTS client: {e}")


def text_to_speech(tts_client, text, filename="output.wav"):
    """
    แปลงข้อความเป็นเสียง wav
    
    Args:
        tts_client: TTS client object
        text (str): ข้อความที่ต้องการแปลง
        filename (str): ชื่อไฟล์เสียงที่จะสร้าง
        
    Returns:
        bool: True หากสำเร็จ, False หากล้มเหลว
    """
    try:
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="th-TH",
            name="th-TH-Chirp3-HD-Erinome"  # เสียง Premium
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000
        )

        response = tts_client.synthesize_speech(
            input=synthesis_input, 
            voice=voice, 
            audio_config=audio_config
        )

        # บันทึกไฟล์ wav
        with open(filename, "wb") as f:
            f.write(response.audio_content)
        
        return True
        
    except Exception as e:
        print(f"❌ ไม่สามารถสร้างเสียงได้: {e}")
        return False


def play_audio(filename):
    """
    เล่นไฟล์เสียงด้วย pygame
    
    Args:
        filename (str): ชื่อไฟล์เสียงที่จะเล่น
        
    Returns:
        bool: True หากเล่นสำเร็จ, False หากล้มเหลว
    """
    if not os.path.exists(filename):
        print(f"❌ ไม่พบไฟล์เสียง: {filename}")
        return False

    try:
        # Initialize pygame mixer
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=16000, size=-16, channels=1, buffer=1024)
        
        # หยุดเสียงก่อนหน้า (ถ้ามี)
        pygame.mixer.music.stop()
        
        # โหลดและเล่นไฟล์
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # รอจนกว่าเสียงเล่นเสร็จ
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        return True
        
    except Exception as e:
        print(f"❌ ไม่สามารถเล่นไฟล์เสียงได้: {e}")
        return False


def cleanup_pygame():
    """ทำความสะอาด pygame mixer"""
    try:
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit()
    except:
        pass


def read_questions(tts_client, questions_array, prefix="question"):
    """
    อ่านคำถามทั้งหมดด้วยเสียง
    
    Args:
        tts_client: TTS client object
        questions_array (list): รายการคำถาม
        prefix (str): prefix สำหรับชื่อไฟล์
        
    Returns:
        bool: True หากสำเร็จ, False หากล้มเหลว
    """
    success = True
    
    for i, question in enumerate(questions_array, 1):
        filename = f"{prefix}_{i}.wav"
        print(f"🔊 กำลังสร้างเสียงสำหรับคำถามที่ {i}...")

        # สร้างเสียง
        if not text_to_speech(tts_client, question, filename):
            print(f"❌ ไม่สามารถสร้างเสียงสำหรับคำถามที่ {i}")
            success = False
            continue

        # เล่นเสียง
        if not play_audio(filename):
            print(f"❌ ไม่สามารถเล่นเสียงสำหรับคำถามที่ {i}")
            success = False
            continue
            
        print(f"✅ เล่นคำถามที่ {i} เรียบร้อย")
        
        # หน่วงเวลาก่อนคำถามถัดไป
        time.sleep(0.5)
    
    return success
