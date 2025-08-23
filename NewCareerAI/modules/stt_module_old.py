#!/usr/bin/env python3
"""
🎤 stt_module_old.py - Legacy Speech-to-Text Module  
====================================================
ฟีเจอร์หลัก:
- Speech Recognition library-based STT
- Simple microphone input handling
- Basic voice recognition functionality
- Google Speech Recognition API integration

ความสามารถ:
- SpeechToText class สำหรับ basic voice recognition
- Real-time microphone input
- Ambient noise adjustment
- Google Speech API integration
- Simple timeout และ phrase limit handling

Limitations:
- Requires internet connection
- Limited to Google Speech API
- Basic functionality only
- No advanced features

Status: DEPRECATED - ใช้ STTmodule.py (Whisper) แทนสำหรับ production
Purpose: Legacy compatibility และ simple testing only
การใช้งาน: from modules.stt_module_old import SpeechToText
====================================================
"""

import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self, timeout=3, phrase_time_limit=5):
        try:
            with sr.Microphone() as source:
                print("🎤 พูดได้เลย...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

            text = self.recognizer.recognize_google(audio, language="th-TH")
            print(f"📝 คุณพูดว่า: {text}")
            return text

        except sr.WaitTimeoutError:
            print("⌛ ไม่ได้ยินเสียงในเวลาที่กำหนด")
            return ""
        except sr.UnknownValueError:
            print("❌ ไม่เข้าใจสิ่งที่พูด")
            return ""
        except Exception as e:
            print(f"🔥 เกิดข้อผิดพลาด: {e}")
            self.recognizer = sr.Recognizer()  # reset ใหม่ถ้า error
            return ""
