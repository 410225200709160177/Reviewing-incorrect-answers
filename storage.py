import json
import os

FILE = "wrong_topics.json"

def save_topic(topic: dict):
    data = load_all_topics()
    data.append(topic)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_all_topics():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
