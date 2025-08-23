#!/usr/bin/env python3
"""
🔊 tts_module_old.py - Legacy Text-to-Speech Module
===================================================
ฟีเจอร์หลัก:
- Simple TTS implementation ด้วย system commands
- macOS built-in TTS support (say command)
- Basic text-to-speech functionality
- Legacy compatibility layer

ความสามารถ:
- TextToSpeech class สำหรับ basic TTS
- macOS "say" command integration
- Simple text output fallback
- Error handling สำหรับ unsupported systems

Limitations:
- macOS only (say command)
- No voice customization
- Basic functionality only
- No audio file output

Status: DEPRECATED - ใช้ TTSmodule.py แทนสำหรับ production
Purpose: Legacy compatibility และ simple testing only
การใช้งาน: from modules.tts_module_old import TextToSpeech
===================================================
"""

import subprocess

class TextToSpeech:
    def speak(self, text):
        try:
            subprocess.run(["say", text])  # macOS built-in TTS
        except Exception as e:
            print(f"⚠️ ไม่สามารถพูดข้อความได้: {e}")

    def speak_text(self, text):
        print(f"🤖 Luna: {text}")
        try:
            subprocess.run(["say", text])  # macOS built-in TTS
        except Exception as e:
            print(f"⚠️ ไม่สามารถพูดข้อความได้: {e}")
