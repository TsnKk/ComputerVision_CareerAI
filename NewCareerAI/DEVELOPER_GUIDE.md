# 👨‍💻 Career AI - Developer Guide
==================================

## 🏗️ สถาปัตยกรรมระบบ

### Core Components
```
├── 🚀 Launchers
│   ├── run_streamlit.py      # Main launcher
│   ├── main.py               # Console launcher
│   └── legacy_main.py        # Legacy compatibility
│
├── 🌐 Web Interface  
│   ├── frontend/app_streamlit.py  # Streamlit app
│   └── frontend/utils.py          # UI utilities
│
├── ⚙️ Core Modules
│   ├── modules/config.py          # Configuration system
│   ├── modules/STTmodule.py       # Speech-to-Text
│   ├── modules/TTSmodule.py       # Text-to-Speech
│   └── core/interview_system.py  # Business logic
│
└── 🛠️ Development Tools
    ├── check_requirements.py     # System validation
    ├── check_api_keys.py         # API validation
    └── test_imports.py           # Import testing
```

---

## 🔧 Development Setup

### 1. Environment Setup
```bash
git clone [repository]
cd NewCareerAI
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Dependencies Installation
```bash
pip install -r requirements.txt
```

### 3. Configuration
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 4. Development Server
```bash
python run_streamlit.py
# or
streamlit run frontend/app_streamlit.py --server.port 8501
```

---

## 📝 Code Architecture

### Configuration System (config.py)
```python
# 5 Main Config Classes:
- APIConfig      # API keys and credentials
- AudioConfig    # Recording/playback settings  
- TTSConfig      # Text-to-speech parameters
- WhisperConfig  # Speech-to-text settings
- InterviewConfig # Interview flow settings
```

### Speech Processing (STTmodule.py)
```python
class WhisperSTT:
    - record_audio()     # Voice recording with VAD
    - transcribe()       # Audio to text conversion
    - get_devices()      # Audio device management
```

### Voice Synthesis (TTSmodule.py)  
```python
class GoogleTTS:
    - synthesize_text()  # Text to speech conversion
    - play_audio()       # Audio playback
    - manage_files()     # Audio file management
```

---

## 🧪 Testing

### Unit Testing
```bash
python test_imports.py       # Module import validation
python check_requirements.py # System requirements
python check_api_keys.py     # API connectivity
```

### Integration Testing
```bash
python examples/google_tts_test.py  # TTS testing
# Manual testing through web interface
```

### Performance Testing
- Monitor memory usage during Whisper model loading
- Test audio recording latency
- Validate API response times

---

## 🔄 Development Workflow

### 1. Feature Development
```bash
# Create feature branch
git checkout -b feature/new-feature

# Develop and test
python check_requirements.py
python run_streamlit.py

# Test specific components
python test_imports.py
```

### 2. Code Quality
```bash
# Format code (if using black)
black *.py modules/ frontend/

# Lint code (if using flake8)
flake8 *.py modules/ frontend/
```

### 3. Documentation Updates
- Update docstrings in code
- Update USER_GUIDE.md for user-facing changes
- Update this DEVELOPER_GUIDE.md for architecture changes

---

## 🐛 Debugging

### Common Debug Points
1. **Module Import Issues**
   ```python
   # Add debug prints in problematic modules
   print(f"Loading module: {__name__}")
   ```

2. **API Connection Problems**
   ```python
   # Enable debug mode in .env
   DEBUG=True
   ```

3. **Audio Issues**
   ```python
   # Check available audio devices
   import sounddevice as sd
   print(sd.query_devices())
   ```

### Logging
```python
# Enable verbose logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📦 Deployment

### Development Deployment
```bash
python run_streamlit.py
# Access: http://localhost:8501
```

### Production Deployment
```bash
# Update requirements
pip freeze > requirements.txt

# Production environment variables
cp .env.example .env.production
# Configure production API keys

# Deploy with proper web server (nginx + gunicorn)
```

### Docker Deployment (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run_streamlit.py"]
```

---

## 🔐 Security Considerations

### API Keys Management
- Never commit `.env` files
- Use environment variables in production
- Rotate API keys regularly
- Implement API rate limiting

### Audio Data Security
- Audio files are stored locally only
- Implement cleanup of temporary files
- Consider encryption for sensitive audio data

---

## 📊 Performance Optimization

### Whisper Model Optimization
```python
# Choose appropriate model size based on requirements
- tiny: Fastest, lower accuracy
- base: Balanced (default)
- small/medium: Better accuracy
- large: Best accuracy, slower
```

### Memory Management
- Implement model caching
- Clean up audio files regularly
- Monitor memory usage during long sessions

### Streamlit Performance
- Use `@st.cache` for expensive operations
- Implement pagination for large datasets
- Optimize component rendering

---

## 🔄 API Integration

### Gemini AI Integration
```python
import google.generativeai as genai
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
```

### Google Cloud TTS Integration
```python
from google.cloud import texttospeech
client = texttospeech.TextToSpeechClient()
```

### Error Handling Best Practices
```python
try:
    # API call
    response = api_client.call()
except APIError as e:
    logger.error(f"API Error: {e}")
    # Implement fallback mechanism
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    # Handle gracefully
```

---

## 📈 Future Development

### Planned Features
- [ ] Multiple language support
- [ ] Advanced interview analytics
- [ ] User authentication system
- [ ] Interview session recording
- [ ] AI-powered feedback system

### Technical Debt
- [ ] Refactor legacy modules
- [ ] Implement comprehensive unit tests
- [ ] Add API documentation
- [ ] Optimize audio processing pipeline

---

## 🤝 Contributing Guidelines

### Code Standards
- Follow PEP 8 Python style guide
- Add comprehensive docstrings
- Include type hints where appropriate
- Write unit tests for new features

### Commit Messages
```
feat: add new feature
fix: resolve bug
docs: update documentation
refactor: improve code structure
test: add testing
```

### Pull Request Process
1. Create feature branch from main
2. Implement feature with tests
3. Update documentation
4. Submit pull request with description

---

**Developer Guide Version**: 1.0.0  
**Last Updated**: August 23, 2025  
**Maintainer**: Career AI Team
