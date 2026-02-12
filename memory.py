import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def update_name(memory, user_input):
    if "my name is" in user_input.lower():
        name = user_input.lower().split("my name is")[-1].strip().title()
        memory["name"] = name
        save_memory(memory)
    return memory
