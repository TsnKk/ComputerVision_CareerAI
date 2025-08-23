@echo off
REM ============================================================
REM 🚀 launch.bat - Windows Auto-Launch Script for Career AI
REM ============================================================
REM ฟีเจอร์หลัก:
REM - Complete system validation and setup
REM - Automatic Python environment checking
REM - Dependency installation and verification
REM - One-click Career AI application launch
REM - Error handling and troubleshooting guidance
REM 
REM ความสามารถ:
REM - Python & pip installation verification
REM - Project files and structure validation  
REM - requirements.txt automatic installation
REM - .env configuration checking and creation
REM - Audio directory setup
REM - Streamlit application auto-launch
REM 
REM การใช้งาน: double-click launch.bat
REM Output: Career AI running at http://localhost:8501
REM ============================================================

echo ============================================================
echo 🚀 Career AI - Auto Setup ^& Launch
echo ============================================================
echo.

REM Check Python installation
echo 1. Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do echo ✅ Python found: %%i
)

echo.
echo 2. Checking pip installation...
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip not found! Please install pip
    pause
    exit /b 1
) else (
    echo ✅ pip is available
)

REM Navigate to project directory
echo.
echo 3. Navigating to project directory...
cd /d "%~dp0"
echo ✅ Current directory: %CD%

REM Check project files
echo.
echo 4. Checking project files...
if exist "requirements.txt" (
    echo ✅ requirements.txt found
) else (
    echo ❌ requirements.txt not found!
    pause
    exit /b 1
)

if exist "run_streamlit.py" (
    echo ✅ run_streamlit.py found
) else (
    echo ❌ run_streamlit.py not found!
    pause
    exit /b 1
)

REM Install requirements
echo.
echo 5. Installing/Updating Python packages...
echo ℹ️  This may take a few minutes...
pip install -r requirements.txt --quiet --disable-pip-version-check
if errorlevel 1 (
    echo ⚠️  Failed to install some packages
    echo ⚠️  Continuing anyway...
) else (
    echo ✅ All packages installed successfully
)

REM Check .env file
echo.
echo 6. Checking environment configuration...
if exist ".env" (
    echo ✅ .env file found
    
    REM Check for API key (simplified check)
    findstr /C:"GEMINI_API_KEY=" .env >nul
    if not errorlevel 1 (
        findstr /C:"GEMINI_API_KEY=your_" .env >nul
        if errorlevel 1 (
            echo ✅ Gemini API Key configured
        ) else (
            echo ⚠️  Gemini API Key not configured properly
            echo ℹ️  Please update .env file with your API key
        )
    ) else (
        echo ⚠️  Gemini API Key not found in .env
    )
) else (
    echo ⚠️  .env file not found
    echo ℹ️  Creating sample .env file...
    (
        echo # Gemini API Key ^(Required^)
        echo GEMINI_API_KEY=your_gemini_api_key_here
        echo.
        echo # Google Cloud Credentials ^(Optional^)
        echo GOOGLE_APPLICATION_CREDENTIALS=careerai-469309-9946c52b3f8e.json
        echo.
        echo # Application Settings
        echo DEBUG=False
        echo PORT=8501
    ) > .env
    echo ✅ Sample .env file created
)

REM Check audio directory
echo.
echo 7. Checking audio directory...
if not exist "audio_files" (
    mkdir audio_files
    echo ✅ Created audio_files directory
) else (
    echo ✅ audio_files directory exists
)

REM Launch application
echo.
echo 8. Launching Streamlit application...
echo ℹ️  Starting Career AI Interview Coach...
echo ℹ️  Access the app at: http://localhost:8501
echo ℹ️  Press Ctrl+C to stop the application
echo.

echo ============================================================
echo 🎯 Career AI Ready to Launch!
echo ============================================================
echo.

REM Start the application
python run_streamlit.py

echo.
echo ⏹️  Application stopped
pause
