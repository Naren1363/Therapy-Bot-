import ollama
from emotion import detect_emotion

def generate_response(user_input, model_context, user_memory):

    emotion = detect_emotion(user_input)

    system_prompt = """
You are a calm and supportive therapy assistant.
Be empathetic and supportive.
"""

    if "name" in user_memory:
        system_prompt += f"\nThe user's name is {user_memory['name']}.\n"

    if emotion:
        system_prompt += f"\nThe user appears to be feeling {emotion}. Respond with extra sensitivity.\n"

    messages = [{"role": "system", "content": system_prompt}]
    messages += model_context
    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    return response["message"]["content"]
