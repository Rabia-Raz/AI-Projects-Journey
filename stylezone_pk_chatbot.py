import os
from groq import Groq

# ============================================
#   👗  STYLEZONE PK — Chatbot
#   Run: python stylezone_pk_chatbot.py
#   Pehle install karo: pip install groq
# ============================================

# Apni Groq API Key yahan daalo
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

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

def print_banner():
    print("""
╔══════════════════════════════════════════════╗
║      👗  STYLEZONE PK — Customer Assistant   ║
║                                              ║
║   📍  Lahore        🚚  3-5 Working Days      ║
║   💬  0300-1234567  (WhatsApp & Orders)       ║
╠══════════════════════════════════════════════╣
║  'menu'  likhain — products dekhne ke liye   ║
║  'quit'  likhain — bahar jaane ke liye       ║
╚══════════════════════════════════════════════╝
""")

def show_menu():
    print("""
👗  StyleZone PK — Products

    👗  Lawn Suit    ........  Rs. 2500
    👔  Linen Shirt  ........  Rs. 1800
    👖  Jeans        ........  Rs. 3000
    🩱  Kurta        ........  Rs. 1500

Order: WhatsApp 0300-1234567
Delivery: 3-5 working days
""")

def main():
    print_banner()
    conversation = []

    print("Bot 👗 : Assalam o Alaikum! StyleZone PK mein khush aamdeed!")
    print("         Kya dhundh rahe hain? Main aapki madad karunga! ✨\n")

    while True:
        try:
            user_input = input("Aap 🙂 : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nShukria! StyleZone PK par dobara tashreef layen. 👗")
            break

        if not user_input:
            continue

        if user_input.lower() in {"quit", "exit", "bye", "q"}:
            print("\nBot 👗 : Shukria! StyleZone PK par dobara tashreef layen. 😊")
            break

        if user_input.lower() in {"menu", "products", "list"}:
            show_menu()
            continue

        conversation.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *conversation
                ],
                max_tokens=400,
                temperature=0.7,
            )
            reply = response.choices[0].message.content.strip()
            conversation.append({"role": "assistant", "content": reply})
            print(f"\nBot 👗 : {reply}\n")

        except Exception as e:
            print(f"\n⚠️  Error: {e}")
            print("Groq API key check karein!\n")
            conversation.pop()

if __name__ == "__main__":
    main()
