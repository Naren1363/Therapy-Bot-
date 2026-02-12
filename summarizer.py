import ollama

def summarize_conversation(conversation):

    summary_prompt = """
Summarize the following conversation briefly.
Keep key emotional themes and important facts.
Do not invent information.
"""

    messages = [
        {"role": "system", "content": summary_prompt},
        {"role": "user", "content": str(conversation)}
    ]

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    return response["message"]["content"]
