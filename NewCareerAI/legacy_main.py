#!/usr/bin/env python3
"""
📜 legacy_main.py - Legacy System Compatibility Layer
=====================================================
ฟีเจอร์หลัก:
- Backward compatibility กับ old module structure
- Legacy TTS/STT modules integration
- Old AI processor และ memory system support
- Migration support จาก old architecture

ความสามารถ:
- Legacy module loading (tts_module_old, stt_module_old)
- Old AI processor compatibility (Llama3 support)
- Memory system integration (JSON-based storage)
- Gradual migration path จาก old to new system

Legacy Components:
- TextToSpeech (old implementation)
- SpeechToText (old implementation)  
- AIProcessor (Llama3-based)
- Memory (JSON storage system)

Status: DEPRECATED - ใช้เพื่อ backward compatibility เท่านั้น
Recommendation: ใช้ run_streamlit.py สำหรับ new system
=====================================================
"""

from modules.tts_module_old import TextToSpeech
from modules.stt_module_old import SpeechToText
from modules.ai_module import AIProcessor
from modules.memory import Memory

def main():
    tts = TextToSpeech()
    stt = SpeechToText()
    ai = AIProcessor(model="llama3")
    memory = Memory()

    print("🤖 ระบบเริ่มทำงานแล้ว พูดคำสั่ง 'หยุด' เพื่อจบการทำงาน")

    while True:
        user_text = stt.listen()
        if not user_text:
            continue

        if "หยุด" in user_text:
            tts.speak("ระบบปิดการทำงานแล้วค่ะ")
            break

        response = ai.get_response(user_text)
        tts.speak(response)

        memory.save(user_text, response)

if __name__ == "__main__":
    main()
