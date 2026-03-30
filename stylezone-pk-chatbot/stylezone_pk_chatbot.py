from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """
Tum StyleZone PK online clothing shop ke assistant ho.
Sirf shop ke baare mein baat karo.

SHOP DETAILS:
- Naam     : StyleZone PK
- Jagah    : Lahore
- WhatsApp : 0300-1234567
- Delivery : 3-5 working days

PRODUCTS AUR PRICES:
- Lawn Suit   = Rs. 2500
- Linen Shirt = Rs. 1800
- Jeans       = Rs. 3000
- Kurta       = Rs. 1500

ORDER KARNE KA TARIKA:
- WhatsApp par message karo: 0300-1234567
- Product ka naam aur size batao
- Address do, delivery 3-5 working days mein ho gi

RULES:
1. Sirf shop ke baare mein baat karo.
2. Bahar ka sawaal aaye to kaho:
   "I can only help you with StyleZone PK related queries!"
3. Roman Urdu ya English mein jawab do.
4. Warm aur friendly raho.
"""

client = Groq(api_key=GROQ_API_KEY)
history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("\n" + "="*50)
print("       StyleZone PK Chatbot")
print("="*50)
print("Assalam o Alaikum! StyleZone PK mein khush aamdeed!")
print("Type 'exit' to quit.")
print("="*50 + "\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "exit":
        print("Bot: Shukriya! StyleZone PK par dobara tashreef layen!")
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
