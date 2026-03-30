from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """You are a helpful chatbot ONLY for Karachi Darbar restaurant.
You MUST ONLY answer questions related to Karachi Darbar.
If someone asks about anything outside the restaurant, respond with exactly:
"I can only help you with Karachi Darbar related queries!"

MENU:
- Biryani = 500 Rs
- Nihari = 400 Rs
- Karahi = 800 Rs
- Naan = 50 Rs

TIMINGS: 12pm - 12am, open every day
LOCATION: Karachi, Saddar
TABLE BOOKING: Call 021-1234567

Be warm and friendly. Use Urdu words like Ji, Zaroor, Shukriya occasionally."""

client = Groq(api_key=GROQ_API_KEY)
history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("\n" + "="*50)
print("       Karachi Darbar Chatbot")
print("="*50)
print("Assalam o Alaikum! Welcome to Karachi Darbar!")
print("Type 'exit' to quit.")
print("="*50 + "\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "exit":
        print("Bot: Shukriya! Karachi Darbar mein aapka intezaar rahega!")
        break

    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history,
        max_tokens=500
    )

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    print(f"\nBot: {reply}\n")
