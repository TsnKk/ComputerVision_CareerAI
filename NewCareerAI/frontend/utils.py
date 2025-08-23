"""
utils.py - ฟังก์ชันช่วยเหลือสำหรับ Streamlit App
"""

import streamlit as st
import os
import tempfile
from datetime import datetime

def show_system_info():
    """แสดงข้อมูลระบบ"""
    st.sidebar.header("💾 ข้อมูลระบบ")
    
    import platform
    import pygame
    
    system_info = f"""
    **ระบบปฏิบัติการ:** {platform.system()} {platform.release()}
    **Python:** {platform.python_version()}
    **Pygame:** {pygame.version.ver}
    **เวลา:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    
    st.sidebar.markdown(system_info)

def create_temp_audio_dir():
    """สร้างโฟลเดอร์ temporary สำหรับไฟล์เสียง"""
    temp_dir = os.path.join(tempfile.gettempdir(), "newcareerai_audio")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir

def cleanup_audio_files(directory):
    """ทำความสะอาดไฟล์เสียงใน directory"""
    try:
        for filename in os.listdir(directory):
            if filename.endswith(('.wav', '.mp3')):
                file_path = os.path.join(directory, filename)
                os.remove(file_path)
        return True
    except Exception as e:
        st.error(f"❌ ไม่สามารถลบไฟล์เสียงได้: {e}")
        return False

def display_progress_bar(current, total):
    """แสดง progress bar แบบสวย"""
    progress = current / total if total > 0 else 0
    
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.progress(progress)
    with col2:
        st.write(f"{current}/{total}")
    with col3:
        st.write(f"{progress*100:.0f}%")

def show_audio_controls():
    """แสดงปุ่มควบคุมเสียง"""
    st.sidebar.header("🎵 การควบคุมเสียง")
    
    # ปรับระดับเสียง (placeholder - pygame ไม่รองรับการปรับระดับเสียงโดยตรง)
    volume = st.sidebar.slider("ระดับเสียง", 0, 100, 80, help="การปรับระดับเสียง (อาจไม่มีผลบางระบบ)")
    
    # ตัวเลือกเสียง TTS
    voice_options = {
        "th-TH-Chirp3-HD-Erinome": "Erinome (แนะนำ)",
        "th-TH-Chirp3-HD-Sulafat": "Sulafat",
        "th-TH-Chirp3-HD-Schedar": "Schedar"
    }
    
    selected_voice = st.sidebar.selectbox(
        "เลือกเสียง TTS:",
        options=list(voice_options.keys()),
        format_func=lambda x: voice_options[x],
        help="เลือกเสียงสำหรับการอ่านคำถาม"
    )
    
    return volume, selected_voice

def format_time_duration(seconds):
    """แปลงวินาทีเป็นรูปแบบ MM:SS"""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def validate_jd_input(jd_text):
    """ตรวจสอบความถูกต้องของ Job Description"""
    errors = []
    
    if not jd_text.strip():
        errors.append("กรุณากรอก Job Description")
    elif len(jd_text.strip()) < 50:
        errors.append("Job Description สั้นเกินไป (ต้องมีอย่างน้อย 50 ตัวอักษร)")
    elif len(jd_text.strip()) > 5000:
        errors.append("Job Description ยาวเกินไป (ไม่เกิน 5000 ตัวอักษร)")
    
    return errors

def show_tips():
    """แสดงคำแนะนำการใช้งาน"""
    with st.expander("💡 คำแนะนำการใช้งาน"):
        st.markdown("""
        ### 📋 การเตรียม Job Description:
        - ควรมีข้อมูลครบถ้วน: ตำแหน่งงาน, หน้าที่รับผิดชอบ, คุณสมบัติที่ต้องการ
        - หลีกเลี่ยงข้อมูลที่ไม่จำเป็น เช่น เงินเดือน, สวัสดิการ
        - ความยาวประมาณ 200-1000 คำ
        
        ### 🎤 การใช้งานไมโครโฟน:
        - ทดสอบไมโครโฟนก่อนเริ่มสัมภาษณ์
        - พูดให้ชัดเจนและไม่เร็วเกินไป
        - หลีกเลี่ยงเสียงรบกวนจากสิ่งแวดล้อม
        
        ### 🔊 การฟังคำถาม:
        - คลิก "ฟังคำถาม" เพื่อให้ AI อ่านคำถาม
        - สามารถฟังซ้ำได้หากไม่ได้ยินชัดเจน
        
        ### 💬 การตอบคำถาม:
        - คิดก่อนตอบ สามารถใช้เวลาได้ตามต้องการ
        - ตอบให้ครบถ้วนและตรงประเด็น
        - หากไม่พอใจคำตอบ สามารถบันทึกใหม่ได้
        
        ### 📊 การดูผลลัพธ์:
        - รอให้ตอบครบทุกคำถามก่อนดูสรุปผล
        - AI จะวิเคราะห์และให้คำแนะนำ
        - สามารถบันทึกผลลัพธ์ไว้ทบทวนได้
        """)

def export_interview_results(questions, answers, summary=""):
    """ส่งออกผลการสัมภาษณ์เป็นไฟล์ text"""
    content = []
    content.append("=" * 60)
    content.append("📋 ผลการสัมภาษณ์งาน - AI Coach for Interview")
    content.append("=" * 60)
    content.append(f"📅 วันที่: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    content.append("")
    
    content.append("❓ คำถามและคำตอบ:")
    content.append("-" * 40)
    
    for i, (q, a) in enumerate(zip(questions, answers), 1):
        content.append(f"\n{i}. {q}")
        content.append(f"   💬 คำตอบ: {a}")
    
    if summary:
        content.append("\n" + "=" * 60)
        content.append("📊 การวิเคราะห์โดย AI:")
        content.append("=" * 60)
        content.append(summary)
    
    content.append("\n" + "=" * 60)
    content.append("🎤 สร้างโดย AI Coach for Interview")
    content.append("=" * 60)
    
    return "\n".join(content)
