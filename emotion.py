def detect_emotion(user_input):

    text = user_input.lower()

    if any(word in text for word in ["sad", "depressed", "down", "unhappy"]):
        return "sad"

    if any(word in text for word in ["anxious", "worried", "nervous", "stress"]):
        return "anxious"

    if any(word in text for word in ["angry", "mad", "frustrated"]):
        return "angry"

    if any(word in text for word in ["tired", "exhausted", "burnt out"]):
        return "tired"

    return None
