import json
import os

SAVE_FILE = "money_save.json"

def save_progress(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_progress():
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        return json.load(f)
