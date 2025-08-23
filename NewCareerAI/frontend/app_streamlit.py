#!/usr/bin/env python3
"""
🎯 app_streamlit.py - AI Interview Coach Web Application
=======================================================
ฟีเจอร์หลัก:
- AI-powered interview question generation (Gemini AI)
- Real-time voice recording and transcription (Whisper STT)
- Text-to-speech response synthesis (Google TTS)
- Interactive job description analysis
- Complete interview simulation workflow
- Audio file management and playback

ความสามารถ:
- Multi-stage interview question generation
- Voice recording with silence detection
- Real-time audio transcription
- Job requirements analysis
- Interview performance tracking
- Audio file download and management
- Responsive web interface with Streamlit

เทคโนโลยี:
- Streamlit (Web Framework)
- Google Generative AI (Question Generation)
- OpenAI Whisper (Speech-to-Text)
- Google Cloud TTS (Text-to-Speech)
- pygame (Audio Playback)
- sounddevice (Audio Recording)

URL: http://localhost:8501
=======================================================
"""

import streamlit as st
import os
import sys
import time
import threading
from io import BytesIO
from pathlib import Path

# โหลด environment variables จากไฟล์ .env
try:
    from dotenv import load_dotenv
    # หา path ของไฟล์ .env
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ โหลดการตั้งค่าจาก {env_path}")
    else:
        print(f"⚠️  ไม่พบไฟล์ .env ที่ {env_path}")
except ImportError:
    print("⚠️  python-dotenv ไม่ได้ติดตั้ง กำลังใช้ system environment variables")

import google.generativeai as genai

# เพิ่ม path สำหรับ modules
import importlib.util
import sys
from pathlib import Path

def import_module_from_file(module_name, file_path):
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            raise ImportError(f"Could not load spec for module {module_name} from {file_path}")
        
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        st.error(f"Error importing {module_name} from {file_path}: {e}")
        return None

# Import modules
try:
    parent_dir = Path(__file__).parent.parent
    
    config = import_module_from_file("config", str(parent_dir / "modules" / "config.py"))
    TTSmodule = import_module_from_file("TTSmodule", str(parent_dir / "modules" / "TTSmodule.py"))
    STTmodule = import_module_from_file("STTmodule", str(parent_dir / "modules" / "STTmodule.py"))
    
    # Get specific functions and variables
    validate_config = config.validate_config
    print_config_status = config.print_config_status
    GEMINI_API_KEY = config.GEMINI_API_KEY
    GOOGLE_CREDENTIALS_PATH = config.GOOGLE_CREDENTIALS_PATH
    INTERVIEW_CONFIG = config.INTERVIEW_CONFIG
    TTS_CONFIG = config.TTS_CONFIG
    
    # TTS functions
    create_tts_client = TTSmodule.create_tts_client
    text_to_speech = TTSmodule.text_to_speech
    play_audio = TTSmodule.play_audio
    
    # STT functions
    record_voice = STTmodule.record_voice
    transcribe_voice = STTmodule.transcribe_voice
    test_microphone = STTmodule.test_microphone
    
except ImportError as e:
    st.error(f"❌ ไม่สามารถโหลดโมดูลได้: {e}")
    st.error(f"Module search paths: {sys.path}")
    st.stop()

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="AI Coach for Interview",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS สำหรับปรับแต่งหน้าเว็บ
st.markdown("""
<style>
.main-header {
    text-align: center;
    color: #1f77b4;
    font-size: 3em;
    font-weight: bold;
    margin-bottom: 0.5em;
}
.sub-header {
    text-align: center;
    color: #666;
    font-size: 1.2em;
    margin-bottom: 2em;
}
.question-box {
    background-color: #f0f8ff;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #1f77b4;
    margin: 10px 0;
}
.answer-box {
    background-color: #f8f8f8;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #28a745;
    margin: 10px 0;
}
.status-success {
    color: #28a745;
    font-weight: bold;
}
.status-error {
    color: #dc3545;
    font-weight: bold;
}
.status-warning {
    color: #ffc107;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ฟังก์ชันสำหรับสร้างคำถามด้วย Gemini
def generate_questions(jd_text):
    """สร้างคำถามจาก JD ด้วย Gemini AI"""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(INTERVIEW_CONFIG["gemini_model"])
        
        prompt = f"""
        กรุณาสร้างคำถามสัมภาษณ์งาน {INTERVIEW_CONFIG["max_questions"]} ข้อ จาก Job Description ข้างล่างนี้
        ให้คำถามเป็นประโยคชัดเจน ไม่ยาวและไม่สั้นเกินไป และเหมาะสมสำหรับถามผู้สมัคร 
        เป็นภาษาไทย ไม่ต้องมีคำอธิบายเพิ่มเติม ขอแค่เฉพาะคำถามตามจำนวนข้อที่กำหนด
        แต่ละคำถามขึ้นบรรทัดใหม่ ไม่ต้องใส่เลขข้อ

        Job Description:
        {jd_text}
        """
        
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # แยกบรรทัดและกรองคำถาม
        questions = []
        for line in text.split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("**"):
                # เอาเลขข้อออก (ถ้ามี)
                import re
                line = re.sub(r'^\d+[\.\)]\s*', '', line)
                questions.append(line)
        
        return questions[:INTERVIEW_CONFIG["max_questions"]]
        
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาดในการสร้างคำถาม: {e}")
        return []

# ฟังก์ชันสำหรับสรุปผลการสัมภาษณ์
def generate_interview_summary(questions, answers):
    """สรุปผลการสัมภาษณ์ด้วย Gemini AI"""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(INTERVIEW_CONFIG["gemini_model"])
        
        qa_text = ""
        for i, (q, a) in enumerate(zip(questions, answers), 1):
            qa_text += f"\nคำถามที่ {i}: {q}\nคำตอบ: {a}\n"
        
        prompt = f"""
        กรุณาวิเคราะห์และสรุปผลการสัมภาษณ์งานจากคำถาม-คำตอบข้างล่างนี้:
        {qa_text}
        
        ให้สรุปในหัวข้อดังนี้:
        1. ความมั่นใจในการตอบคำถาม (1-10)
        2. ความสมบูรณ์ของคำตอบ (1-10)
        3. จุดแข็งที่พบ
        4. จุดที่ควรปรับปรุง
        5. คำแนะนำสำหรับการสัมภาษณ์ครั้งต่อไป
        
        ให้คำตอบเป็นภาษาไทย มีการจัดรูปแบบที่อ่านง่าย
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาดในการสรุปผล: {e}"

# Initialize session state
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'interview_started' not in st.session_state:
    st.session_state.interview_started = False
if 'interview_completed' not in st.session_state:
    st.session_state.interview_completed = False
if 'tts_client' not in st.session_state:
    st.session_state.tts_client = None

# หัวข้อหลัก
st.markdown('<div class="main-header">🎤 AI Coach for Interview</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">ระบบฝึกสัมภาษณ์งานด้วย AI</div>', unsafe_allow_html=True)

# Sidebar สำหรับการตั้งค่า
with st.sidebar:
    st.header("⚙️ การตั้งค่าระบบ")
    
    # ตรวจสอบการตั้งค่า
    config_errors = validate_config()
    if config_errors:
        st.error("❌ พบปัญหาการตั้งค่า:")
        for error in config_errors:
            st.write(f"- {error}")
        
        st.info("💡 วิธีแก้ไข:")
        st.code("""
# ตั้งค่า Environment Variables
set GEMINI_API_KEY=your_api_key
set GOOGLE_APPLICATION_CREDENTIALS=path_to_service_account.json
        """)
    else:
        st.success("✅ การตั้งค่าถูกต้อง")
    
    # ทดสอบไมโครโฟน
    st.subheader("🎤 ทดสอบไมโครโฟน")
    if st.button("ทดสอบไมโครโฟน"):
        with st.spinner("กำลังทดสอบ..."):
            if test_microphone():
                st.success("✅ ไมโครโฟนทำงานปกติ")
            else:
                st.error("❌ ไมโครโฟนมีปัญหา")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    # ส่วนกรอก Job Description
    st.header("📋 1. กรอก Job Description")
    jd_text = st.text_area(
        "กรอก Job Description ที่ต้องการฝึกสัมภาษณ์:",
        height=200,
        placeholder="วางข้อมูล Job Description ที่นี่..."
    )
    
    # ปุ่มสร้างคำถาม
    if st.button("🤖 สร้างคำถามด้วย AI", type="primary"):
        if not jd_text.strip():
            st.error("❌ กรุณากรอก Job Description ก่อน!")
        elif config_errors:
            st.error("❌ กรุณาแก้ไขการตั้งค่าก่อน!")
        else:
            with st.spinner("🧠 AI กำลังสร้างคำถาม..."):
                questions = generate_questions(jd_text)
                if questions:
                    st.session_state.questions = questions
                    st.session_state.answers = [""] * len(questions)
                    st.session_state.current_question = 0
                    st.session_state.interview_started = False
                    st.session_state.interview_completed = False
                    st.success(f"✅ สร้างคำถาม {len(questions)} ข้อ สำเร็จ!")
                else:
                    st.error("❌ ไม่สามารถสร้างคำถามได้")
    
    # แสดงคำถามที่สร้างได้
    if st.session_state.questions:
        st.header("❓ 2. คำถามที่สร้างโดย AI")
        for i, question in enumerate(st.session_state.questions, 1):
            st.markdown(f'<div class="question-box"><strong>คำถามที่ {i}:</strong> {question}</div>', 
                       unsafe_allow_html=True)
        
        # ปุ่มเริ่มสัมภาษณ์
        if not st.session_state.interview_started and not st.session_state.interview_completed:
            if st.button("🎯 เริ่มการสัมภาษณ์", type="primary"):
                try:
                    # สร้าง TTS client
                    st.session_state.tts_client = create_tts_client(GOOGLE_CREDENTIALS_PATH)
                    st.session_state.interview_started = True
                    st.success("✅ เริ่มการสัมภาษณ์แล้ว!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ ไม่สามารถเริ่มการสัมภาษณ์ได้: {e}")
        
        # ส่วนการสัมภาษณ์
        if st.session_state.interview_started and not st.session_state.interview_completed:
            st.header("🎤 3. การสัมภาษณ์")
            
            current_q = st.session_state.current_question
            total_q = len(st.session_state.questions)
            
            st.progress((current_q) / total_q)
            st.write(f"**คำถามที่ {current_q + 1} จาก {total_q}**")
            
            current_question = st.session_state.questions[current_q]
            st.markdown(f'<div class="question-box"><strong>คำถาม:</strong> {current_question}</div>', 
                       unsafe_allow_html=True)
            
            col_tts, col_record = st.columns(2)
            
            with col_tts:
                if st.button("🔊 ฟังคำถาม"):
                    with st.spinner("กำลังสร้างเสียง..."):
                        try:
                            filename = f"question_{current_q + 1}.wav"
                            if text_to_speech(st.session_state.tts_client, current_question, filename):
                                if play_audio(filename):
                                    st.success("✅ เล่นเสียงสำเร็จ")
                                else:
                                    st.error("❌ ไม่สามารถเล่นเสียงได้")
                            else:
                                st.error("❌ ไม่สามารถสร้างเสียงได้")
                        except Exception as e:
                            st.error(f"❌ เกิดข้อผิดพลาด: {e}")
            
            with col_record:
                if st.button("🎤 บันทึกคำตอบ"):
                    with st.spinner("กำลังบันทึกเสียง... (พูดได้เลย)"):
                        try:
                            audio_file = record_voice(f"answer_{current_q + 1}.wav")
                            if audio_file:
                                with st.spinner("กำลังแปลงเสียงเป็นข้อความ..."):
                                    answer = transcribe_voice(audio_file)
                                    if answer:
                                        st.session_state.answers[current_q] = answer
                                        st.success("✅ บันทึกคำตอบสำเร็จ!")
                                        st.rerun()
                                    else:
                                        st.error("❌ ไม่สามารถแปลงเสียงเป็นข้อความได้")
                            else:
                                st.error("❌ การบันทึกเสียงล้มเหลว")
                        except Exception as e:
                            st.error(f"❌ เกิดข้อผิดพลาด: {e}")
            
            # แสดงคำตอบปัจจุบัน
            if st.session_state.answers[current_q]:
                st.markdown(f'<div class="answer-box"><strong>คำตอบของคุณ:</strong> {st.session_state.answers[current_q]}</div>', 
                           unsafe_allow_html=True)
                
                col_prev, col_next = st.columns(2)
                
                with col_prev:
                    if current_q > 0:
                        if st.button("⬅️ คำถามก่อนหน้า"):
                            st.session_state.current_question -= 1
                            st.rerun()
                
                with col_next:
                    if current_q < total_q - 1:
                        if st.button("➡️ คำถามถัดไป"):
                            st.session_state.current_question += 1
                            st.rerun()
                    else:
                        if st.button("🏁 จบการสัมภาษณ์", type="primary"):
                            st.session_state.interview_completed = True
                            st.rerun()
        
        # สรุปผลการสัมภาษณ์
        if st.session_state.interview_completed:
            st.header("📊 4. สรุปผลการสัมภาษณ์")
            
            # แสดงคำถาม-คำตอบทั้งหมด
            st.subheader("💬 คำถามและคำตอบทั้งหมด")
            for i, (q, a) in enumerate(zip(st.session_state.questions, st.session_state.answers), 1):
                with st.expander(f"คำถามที่ {i}"):
                    st.markdown(f'<div class="question-box"><strong>คำถาม:</strong> {q}</div>', 
                               unsafe_allow_html=True)
                    st.markdown(f'<div class="answer-box"><strong>คำตอบ:</strong> {a}</div>', 
                               unsafe_allow_html=True)
            
            # สร้างสรุปผลด้วย AI
            st.subheader("🤖 การวิเคราะห์โดย AI")
            if st.button("📈 สร้างรายงานการวิเคราะห์"):
                with st.spinner("🧠 AI กำลังวิเคราะห์ผลการสัมภาษณ์..."):
                    summary = generate_interview_summary(st.session_state.questions, st.session_state.answers)
                    st.markdown("### 📋 รายงานการวิเคราะห์")
                    st.markdown(summary)
            
            # ปุ่มเริ่มใหม่
            if st.button("🔄 เริ่มการสัมภาษณ์ใหม่", type="secondary"):
                # Reset session state
                st.session_state.questions = []
                st.session_state.answers = []
                st.session_state.current_question = 0
                st.session_state.interview_started = False
                st.session_state.interview_completed = False
                st.session_state.tts_client = None
                st.rerun()

with col2:
    st.header("📊 สถิติการใช้งาน")
    
    if st.session_state.questions:
        total_questions = len(st.session_state.questions)
        answered_questions = sum(1 for answer in st.session_state.answers if answer.strip())
        
        # Progress metrics
        st.metric("จำนวนคำถามทั้งหมด", total_questions)
        st.metric("ตอบแล้ว", answered_questions)
        st.metric("เหลือ", total_questions - answered_questions)
        
        # Progress bar
        if total_questions > 0:
            progress = answered_questions / total_questions
            st.progress(progress)
            st.write(f"ความคืบหน้า: {progress*100:.1f}%")
    
    # ข้อมูลเทคนิค
    st.header("🔧 ข้อมูลเทคนิค")
    st.info(f"""
    **เทคโนโลยีที่ใช้:**
    - 🤖 Google Gemini AI
    - 🔊 Google Cloud TTS
    - 🎤 OpenAI Whisper STT
    - 🎮 Pygame Audio
    - 🌐 Streamlit Web UI
    
    **การตั้งค่า:**
    - เสียง: {TTS_CONFIG['voice_name']}
    - ภาษา: {TTS_CONFIG['language_code']}
    - คำถามสูงสุด: {INTERVIEW_CONFIG['max_questions']} ข้อ
    """)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666;">'
    '🎤 AI Coach for Interview - ระบบฝึกสัมภาษณ์งานด้วย AI'
    '</div>', 
    unsafe_allow_html=True
)
