#!/usr/bin/env python3
"""
🚀 main.py - NewCareerAI Core Application Launcher  
==================================================
ฟีเจอร์หลัก:
- Primary entry point สำหรับ NewCareerAI system
- Module path management และ system initialization
- Alternative launcher สำหรับ console-based interface
- Development และ testing entry point

ความสามารถ:
- System path configuration และ module loading
- Console-based interview system launch
- Development environment setup
- Command-line interface สำหรับ advanced users
- Integration testing และ debugging utilities

ส่วนประกอบหลัก:
- Module path initialization
- Core system bootstrapping  
- Development tools และ utilities
- Legacy compatibility functions

การใช้งาน: python main.py
Note: สำหรับ web interface ให้ใช้ run_streamlit.py แทน
==================================================
"""
import os
import sys

# เพิ่ม modules และ core path
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_path = os.path.join(current_dir, 'modules')
core_path = os.path.join(current_dir, 'core')

sys.path.insert(0, modules_path)
sys.path.insert(0, core_path)

def main():
    """ฟังก์ชันหลักสำหรับเริ่มระบบ"""
    
    print("=" * 60)
    print("🚀 NewCareerAI - ระบบสัมภาษณ์งานขั้นสูงด้วย AI")
    print("=" * 60)
    
    # ตรวจสอบการตั้งค่า
    try:
        from config import validate_config, print_config_status
        
        print_config_status()
        errors = validate_config()
        
        if errors:
            print("❌ พบปัญหาการตั้งค่า:")
            for error in errors:
                print(f"   - {error}")
            print("\n💡 วิธีแก้ไข:")
            print("   1. ตั้งค่า environment variables:")
            print("      set GEMINI_API_KEY=your_api_key")
            print("      set GOOGLE_APPLICATION_CREDENTIALS=path_to_service_account.json")
            print("   2. หรือใส่ไฟล์ service account ในโฟลเดอร์โปรเจค")
            return False
            
    except ImportError as e:
        print(f"❌ ไม่สามารถโหลดโมดูลการตั้งค่า: {e}")
        return False
    
    # เริ่มระบบสัมภาษณ์
    try:
        from interview_system import main as interview_main
        
        print("\n🎯 เริ่มต้นระบบสัมภาษณ์งาน...")
        success = interview_main()
        
        if success:
            print("\n🎉 ระบบทำงานเสร็จสิ้นสมบูรณ์!")
            return True
        else:
            print("\n❌ ระบบทำงานไม่สมบูรณ์")
            return False
            
    except ImportError as e:
        print(f"❌ ไม่สามารถโหลดระบบสัมภาษณ์: {e}")
        return False
    except KeyboardInterrupt:
        print("\n⏹️  ผู้ใช้หยุดการทำงาน")
        return False
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดไม่คาดคิด: {e}")
        return False

if __name__ == "__main__":
    try:
        success = main()
        exit_code = 0 if success else 1
        print(f"\n{'='*60}")
        print(f"🏁 สิ้นสุดการทำงาน (Exit Code: {exit_code})")
        print(f"{'='*60}")
        exit(exit_code)
        
    except KeyboardInterrupt:
        print("\n⏹️  หยุดการทำงานด้วยผู้ใช้")
        exit(1)
    except Exception as e:
        print(f"\n💥 เกิดข้อผิดพลาดร้ายแรง: {e}")
        exit(1)
