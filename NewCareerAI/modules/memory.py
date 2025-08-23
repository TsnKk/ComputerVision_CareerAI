#!/usr/bin/env python3
"""
💾 memory.py - Legacy JSON-based Memory System
==============================================
ฟีเจอร์หลัก:
- JSON-based conversation memory storage
- Session management และ history tracking
- File-based persistent storage system
- Legacy memory interface สำหรับ old AI system

ความสามารถ:
- Memory class สำหรับ conversation history management
- JSON file-based storage (data/memory.json)
- Session timestamp tracking
- Conversation history persistence
- Legacy compatibility สำหรับ old AI modules

Storage Structure:
- JSON format conversation logs
- Timestamped entries
- File-based persistence
- Simple key-value memory system

Status: LEGACY - สำหรับ backward compatibility
Current System: ใช้ Streamlit session state แทน
การใช้งาน: from modules.memory import Memory (Legacy only)
==============================================
"""

import json
import os
from datetime import datetime

class Memory:
    def __init__(self, file_path=None):
        if file_path is None:
            # ใช้ data/memory.json ในโปรเจ็กต์
            current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.file_path = os.path.join(current_dir, "data", "memory.json")
        else:
            self.file_path = file_path

    def save(self, question, answer):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "question": question,
            "answer": answer
        }
        data.append(entry)

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
