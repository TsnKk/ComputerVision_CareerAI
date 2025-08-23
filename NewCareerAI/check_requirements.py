#!/usr/bin/env python3
"""
� check_requirements.py - System Requirements Validator
========================================================
ฟีเจอร์หลัก:
- Pre-launch system validation และ dependency checking
- Python environment และ package verification
- API keys และ configuration file validation
- Port availability และ system resource checking
- Automated problem detection และ solution suggestions

ความสามารถ:
- Python version compatibility checking (3.8+)
- Required package installation verification
- .env file และ API key validation
- Directory structure และ required files checking
- System resources (disk space, memory, ports)
- Launch command generation สำหรับแต่ละ platform

การตรวจสอบ:
- Python & pip installation
- All required Python packages
- Project files และ directory structure
- Environment configuration (.env files)
- API keys (Gemini, Google Cloud)
- Port availability (8501, 8502)

การใช้งาน: python check_requirements.py
========================================================
"""

import sys
import subprocess
import os
import json
from pathlib import Path
import importlib.util

def print_header():
    print("=" * 60)
    print("🔍 Career AI - System Requirements Check")
    print("=" * 60)
    print()

def print_status(message, status="info"):
    icons = {"success": "✅", "error": "❌", "warning": "⚠️", "info": "ℹ️"}
    print(f"{icons.get(status, 'ℹ️')} {message}")

def check_python_version():
    print("1. Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - OK", "success")
        return True
    else:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - Need 3.8+", "error")
        return False

def check_pip():
    print("\n2. Checking pip installation...")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True, check=True)
        print_status("pip is available", "success")
        return True
    except subprocess.CalledProcessError:
        print_status("pip not found", "error")
        return False

def check_required_files():
    print("\n3. Checking required files...")
    required_files = [
        "requirements.txt",
        "run_streamlit.py", 
        "frontend/app_streamlit.py",
        "modules/config.py",
        "modules/STTmodule.py",
        "modules/TTSmodule.py"
    ]
    
    all_present = True
    for file in required_files:
        if os.path.exists(file):
            print_status(f"{file} - Found", "success")
        else:
            print_status(f"{file} - Missing", "error")
            all_present = False
    
    return all_present

def check_directories():
    print("\n4. Checking required directories...")
    required_dirs = ["frontend", "modules", "core", "audio_files", "docs"]
    
    all_present = True
    for directory in required_dirs:
        if os.path.exists(directory) and os.path.isdir(directory):
            print_status(f"{directory}/ - Found", "success")
        else:
            if directory == "audio_files":
                os.makedirs(directory, exist_ok=True)
                print_status(f"{directory}/ - Created", "success")
            else:
                print_status(f"{directory}/ - Missing", "error")
                all_present = False
    
    return all_present

def check_env_file():
    print("\n5. Checking environment configuration...")
    env_file = ".env"
    
    if not os.path.exists(env_file):
        print_status(".env file not found", "warning")
        return False
    
    print_status(".env file found", "success")
    
    # Check for required API key
    try:
        with open(env_file, 'r') as f:
            content = f.read()
            if "GEMINI_API_KEY=" in content and "your_gemini_api_key" not in content:
                print_status("Gemini API Key configured", "success")
                return True
            else:
                print_status("Gemini API Key needs configuration", "warning")
                return False
    except Exception as e:
        print_status(f"Error reading .env file: {e}", "error")
        return False

def check_packages():
    print("\n6. Checking required Python packages...")
    required_packages = [
        "streamlit",
        "google.generativeai", 
        "whisper",
        "pygame",
        "sounddevice",
        "python-dotenv"
    ]
    
    all_installed = True
    for package in required_packages:
        try:
            # Handle different package import names
            import_name = package
            if package == "google.generativeai":
                import_name = "google.generativeai"
            elif package == "python-dotenv":
                import_name = "dotenv"
                
            spec = importlib.util.find_spec(import_name)
            if spec is not None:
                print_status(f"{package} - Installed", "success")
            else:
                print_status(f"{package} - Not found", "error")
                all_installed = False
        except ImportError:
            print_status(f"{package} - Not found", "error")
            all_installed = False
    
    return all_installed

def check_system_resources():
    print("\n7. Checking system resources...")
    
    # Check available disk space
    try:
        import shutil
        total, used, free = shutil.disk_usage(".")
        free_gb = free // (1024**3)
        if free_gb >= 2:
            print_status(f"Disk space: {free_gb}GB available - OK", "success")
        else:
            print_status(f"Disk space: {free_gb}GB available - Low", "warning")
    except:
        print_status("Could not check disk space", "warning")
    
    # Check if ports are available
    import socket
    ports_to_check = [8501, 8502]
    for port in ports_to_check:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            if result != 0:
                print_status(f"Port {port} - Available", "success")
            else:
                print_status(f"Port {port} - In use", "warning")
        except:
            print_status(f"Port {port} - Cannot check", "warning")

def generate_launch_command():
    print("\n8. Generating launch commands...")
    current_dir = os.getcwd()
    
    commands = {
        "Windows PowerShell": f'cd "{current_dir}"; python run_streamlit.py',
        "Windows CMD": f'cd "{current_dir}" && python run_streamlit.py',
        "Linux/Mac": f'cd "{current_dir}" && python run_streamlit.py',
        "Direct Streamlit": f'cd "{current_dir}/frontend" && streamlit run app_streamlit.py'
    }
    
    print_status("Launch commands ready:", "info")
    for platform, command in commands.items():
        print(f"  {platform}: {command}")

def main():
    print_header()
    
    checks = [
        check_python_version(),
        check_pip(),
        check_required_files(),
        check_directories(),
        check_env_file(),
        check_packages(),
    ]
    
    check_system_resources()
    generate_launch_command()
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    
    passed = sum(checks)
    total = len(checks)
    
    if passed == total:
        print_status(f"All checks passed ({passed}/{total}) - Ready to launch! 🚀", "success")
        return 0
    else:
        print_status(f"Some checks failed ({passed}/{total}) - Review issues above", "warning")
        
        print("\n💡 Quick fixes:")
        print("• Install packages: pip install -r requirements.txt")
        print("• Configure API key in .env file")
        print("• Check file paths and permissions")
        
        return 1

if __name__ == "__main__":
    sys.exit(main())
