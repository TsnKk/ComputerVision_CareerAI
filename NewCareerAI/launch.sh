#!/bin/bash
#=============================================================
# 🚀 launch.sh - Unix/Linux Auto-Launch Script for Career AI
#=============================================================
# ฟีเจอร์หลัก:
# - Complete system validation and setup for Unix/Linux/Mac
# - Automatic Python environment checking
# - Dependency installation and verification
# - One-click Career AI application launch
# - Colored output and error handling
# 
# ความสามารถ:
# - Python & pip installation verification
# - Project files and structure validation  
# - requirements.txt automatic installation
# - .env configuration checking and creation
# - Audio directory setup
# - Cross-platform compatibility (Linux/Mac/Unix)
# - Streamlit application auto-launch
# 
# การใช้งาน: bash launch.sh
# Output: Career AI running at http://localhost:8501
#=============================================================

# 🚀 Career AI - Streamlit Launch Script
# Auto-setup and launch script for NewCareerAI application

echo "============================================================"
echo "🚀 Career AI - Auto Setup & Launch"
echo "============================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check Python installation
echo "1. Checking Python installation..."
if command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1)
    print_status "Python found: $PYTHON_VERSION"
else
    print_error "Python not found! Please install Python 3.8+"
    exit 1
fi

# Check pip installation
echo ""
echo "2. Checking pip installation..."
if command -v pip &> /dev/null; then
    print_status "pip is available"
else
    print_error "pip not found! Please install pip"
    exit 1
fi

# Navigate to project directory
echo ""
echo "3. Navigating to project directory..."
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"
print_status "Current directory: $(pwd)"

# Check if requirements.txt exists
echo ""
echo "4. Checking project files..."
if [ -f "requirements.txt" ]; then
    print_status "requirements.txt found"
else
    print_error "requirements.txt not found!"
    exit 1
fi

if [ -f "run_streamlit.py" ]; then
    print_status "run_streamlit.py found"
else
    print_error "run_streamlit.py not found!"
    exit 1
fi

# Install requirements
echo ""
echo "5. Installing/Updating Python packages..."
print_info "This may take a few minutes..."
pip install -r requirements.txt --quiet --disable-pip-version-check
if [ $? -eq 0 ]; then
    print_status "All packages installed successfully"
else
    print_error "Failed to install some packages"
    print_warning "Continuing anyway..."
fi

# Check .env file
echo ""
echo "6. Checking environment configuration..."
if [ -f ".env" ]; then
    print_status ".env file found"
    
    # Check for required API key
    if grep -q "GEMINI_API_KEY=" .env && ! grep -q "GEMINI_API_KEY=your_" .env; then
        print_status "Gemini API Key configured"
    else
        print_warning "Gemini API Key not configured properly"
        print_info "Please update .env file with your API key"
    fi
else
    print_warning ".env file not found"
    print_info "Creating sample .env file..."
    cat > .env << EOL
# Gemini API Key (Required)
GEMINI_API_KEY=your_gemini_api_key_here

# Google Cloud Credentials (Optional)
GOOGLE_APPLICATION_CREDENTIALS=careerai-469309-9946c52b3f8e.json

# Application Settings
DEBUG=False
PORT=8501
EOL
    print_status "Sample .env file created"
fi

# Check for audio files directory
echo ""
echo "7. Checking audio directory..."
if [ ! -d "audio_files" ]; then
    mkdir -p audio_files
    print_status "Created audio_files directory"
else
    print_status "audio_files directory exists"
fi

# Launch application
echo ""
echo "8. Launching Streamlit application..."
print_info "Starting Career AI Interview Coach..."
print_info "Access the app at: http://localhost:8501"
print_info "Press Ctrl+C to stop the application"

echo ""
echo "============================================================"
echo "🎯 Career AI Ready to Launch!"
echo "============================================================"

# Start the application
python run_streamlit.py
