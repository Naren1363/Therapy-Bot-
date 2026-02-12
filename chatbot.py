import ollama
import json
import os

print("Therapy Chatbot Started (type 'quit' to exit)\n")

# -------- Memory File Setup --------
memory_file = "memory.json"

# Load memory if it exists
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        user_memory = json.load(f)
else:
    user_memory = {}

conversation = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    # -------- Memory Extraction --------
    if "my name is" in user_input.lower():
        name = user_input.lower().split("my name is")[-1].strip().title()
        user_memory["name"] = name

        with open(memory_file, "w") as f:
            json.dump(user_memory, f)

    if user_input.lower().startswith("i am "):
        name = user_input[5:].strip().title()
        user_memory["name"] = name

        with open(memory_file, "w") as f:
            json.dump(user_memory, f)

    # -------- Direct Memory Answer --------
    if "what is my name" in user_input.lower():
        if "name" in user_memory:
            print(f"Bot: Your name is {user_memory['name']}.")
        else:
            print("Bot: I don't know your name yet. You can tell me!")
        continue

    # -------- Build System Prompt --------
    system_prompt = """
You are a calm and supportive therapy assistant.

RULES:
- Be supportive and empathetic.
- Use user's stored details naturally.
- Do not claim memory loss.
"""

    # Inject memory naturally
    if "name" in user_memory:
        system_prompt += f"\nThe user's name is {user_memory['name']}.\n"

    # -------- Build Messages --------
    messages = [{"role": "system", "content": system_prompt}] + conversation
    messages.append({"role": "user", "content": user_input})

    # -------- AI Response --------
    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    bot_reply = response["message"]["content"]
    print("Bot:", bot_reply)

    # -------- Store Conversation --------
    conversation.append({"role": "user", "content": user_input})
    conversation.append({"role": "assistant", "content": bot_reply})
