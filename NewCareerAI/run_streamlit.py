#!/usr/bin/env python3
"""
🚀 run_streamlit.py - Streamlit Application Launcher
===============================================
ฟีเจอร์หลัก:
- เปิดตัวแอพ AI Interview Coach ผ่าน Streamlit
- ตรวจสอบความพร้อมของระบบก่อนเปิดตัว
- จัดการเส้นทางไฟล์และการตั้งค่าอัตโนมัติ
- แสดงข้อความแนะนำและ URL สำหรับการเข้าถึง

ความสามารถ:
- Auto-launch Streamlit web server
- Built-in error handling and status messages
- Automatic browser opening (configurable)
- Cross-platform compatibility
- Graceful shutdown with Ctrl+C

การใช้งาน: python run_streamlit.py
URL: http://localhost:8501
===============================================
"""

import os
import sys
import subprocess

def main():
    """เปิด Streamlit App"""
    
    print("=" * 60)
    print("🚀 เริ่มต้น AI Coach for Interview")
    print("=" * 60)
    
    # ตรวจสอบว่าติดตั้ง streamlit แล้วหรือไม่
    try:
        import streamlit
        print("✅ Streamlit พร้อมใช้งาน")
    except ImportError:
        print("❌ ไม่พบ Streamlit")
        print("💡 ติดตั้งด้วยคำสั่ง: pip install streamlit")
        return False
    
    # เส้นทางไฟล์ app
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(current_dir, "frontend", "app_streamlit.py")
    
    if not os.path.exists(app_path):
        print(f"❌ ไม่พบไฟล์ app: {app_path}")
        return False
    
    print(f"📁 เส้นทางแอป: {app_path}")
    print("🌐 กำลังเปิดเว็บเบราว์เซอร์...")
    print("📍 URL: http://localhost:8501")
    print("")
    print("⚠️  หากต้องการหยุดการทำงาน กด Ctrl+C")
    print("=" * 60)
    
    # รัน streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", app_path,
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n⏹️  หยุดการทำงานโดยผู้ใช้")
    except Exception as e:
        print(f"\n❌ เกิดข้อผิดพลาด: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)
