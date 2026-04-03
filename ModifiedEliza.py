from nltk.chat.util import Chat, reflections

# Step: 5+ Modified rules for the assignment
pairs = [
    [r"Hello", ["Greetings! How can I assist you today?", "Hello there! What is on your mind?"]],
    [r"my name is (.*)", ["It is nice to meet you, %1. How are you feeling?", "Hello %1, tell me what brings you here."]],
    [r"I feel (.*)", ["Why do you think you feel %1?", "Is feeling %1 something you experience often?"]],
    [r"I am (.*)", ["How long have you been %1?", "What made you %1 right now?"]],
    [r"because (.*)", ["Is that the real reason, or is there more to it?", "How does %1 affect your situation?"]],
    [r"(.*) mother (.*)", ["Tell me more about your mother.", "How do you feel about your mother?"]],
    [r"I need (.*)", ["Why is it important for you to get %1?", "What would change if you had %1?"]],
    [r"quit", ["Goodbye! I hope our talk was helpful."]]
]

def get_eliza_response(user_input: str) -> str:
    chat = Chat(pairs, reflections)
    return chat.respond(user_input)

if __name__ == "__main__":
    print("ELIZA Chatbot (Modified Rules Version)")
    print("Type 'quit' to stop.\n")
    chat = Chat(pairs, reflections)
    chat.converse()