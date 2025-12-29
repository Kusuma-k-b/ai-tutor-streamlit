



from google import genai
from google.genai import types
from google.colab import userdata

# 1. Setup the Client using your Colab Secret
api_key = userdata.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

# 2. Define the Personality (System Instruction)
SYSTEM_PROMPT = """
You are an AI tutor for freshers.
Explain concepts step-by-step.
Use simple language.
Give real-world examples.
If needed, give a short code example.
Ask one follow-up question.
"""

# 3. Create the Chat Session with the correct Config
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
    )
)

print("🎓 Gemini Tutor Chat Started! (Type 'exit' to stop)\n")

# 4. The Conversation Loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Goodbye! Happy learning!")
        break

    # Send the message and get the response
    response = chat.send_message(user_input)

    print(f"\nAI: {response.text}\n")
    print("-" * 30)

