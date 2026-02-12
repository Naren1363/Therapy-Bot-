def check_crisis(user_input):

    text = user_input.lower()

    crisis_keywords = [
        "kill myself",
        "suicide",
        "end my life",
        "hurt myself",
        "self harm",
        "don't want to live"
    ]

    for phrase in crisis_keywords:
        if phrase in text:
            return True

    return False


def crisis_response():
    return (
        "I'm really sorry that you're feeling this way. "
        "You don't have to handle this alone.\n\n"
        "If you're in immediate danger, please contact local emergency services.\n\n"
        "If you're in India, you can call the Kiran Mental Health Helpline: 1800-599-0019.\n\n"
        "You matter, and support is available."
    )
