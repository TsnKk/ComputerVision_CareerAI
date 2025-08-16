import json
from datetime import datetime

class Memory:
    def __init__(self, file_path="memory.json"):
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