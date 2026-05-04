import re
from datetime import datetime

# -----------------------------
# Knowledge Base (Domain Answers)
# -----------------------------
knowledge_base = {
    "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "python": "Python is a high-level programming language used for AI, automation, and web development.",
    "machine learning": "Machine Learning is a subset of AI where systems learn from data.",
    "nlp": "Natural Language Processing helps computers understand human language."
}

# -----------------------------
# Intent Patterns (Regex)
# -----------------------------
patterns = {
    "greeting": r"\b(hi|hello|hey|assalamualaikum)\b",
    "help": r"\b(help|assist|support)\b",
    "goodbye": r"\b(bye|exit|quit|allah hafiz)\b",
    "thanks": r"\b(thanks|thank you)\b",
    "smalltalk": r"\b(how are you|what's up)\b",
    "knowledge": r"\b(ai|python|machine learning|nlp)\b"
}

# -----------------------------
# Responses
# -----------------------------
responses = {
    "greeting": "Hello! How can I assist you today?",
    "help": "I can answer basic questions about AI, Python, ML, and NLP.",
    "goodbye": "Goodbye! Have a great day.",
    "thanks": "You're welcome!",
    "smalltalk": "I'm just a bot, but I'm doing fine!"
}

# -----------------------------
# Detect Intent
# -----------------------------
def detect_intent(user_input):
    for intent, pattern in patterns.items():
        if re.search(pattern, user_input.lower()):
            return intent
    return "unknown"

# -----------------------------
# Generate Response
# -----------------------------
def get_response(user_input):
    intent = detect_intent(user_input)

    if intent == "knowledge":
        for key in knowledge_base:
            if key in user_input.lower():
                return knowledge_base[key]

    return responses.get(intent, "Sorry, I don't understand that.")

# -----------------------------
# Save Chat History
# -----------------------------
def log_chat(user_input, bot_response):
    with open("chat_log.txt", "a") as f:
        f.write(f"{datetime.now()} USER: {user_input}\n")
        f.write(f"{datetime.now()} BOT: {bot_response}\n")

# -----------------------------
# Main Chat Loop
# -----------------------------
def run_chatbot():
    print("=== Simple Rule-Based Chatbot ===")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        log_chat(user_input, response)

        if detect_intent(user_input) == "goodbye":
            break

# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    run_chatbot()