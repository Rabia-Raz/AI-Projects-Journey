from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq

app = Flask(__name__, static_folder=".")
CORS(app)

# ── Apni Groq API Key yahan daalo ──
GROQ_API_KEY = "YOUR_API_KEY_HERE"
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
Tum StyleZone PK online clothing shop ke official AI assistant ho.
Tumhara kaam sirf shop ke baare mein customers ki madad karna hai.

Jawab us language mein do jismein customer baat kare:
- Roman Urdu mein likhe to Roman Urdu mein jawab do
- English mein likhe to English mein jawab do

SHOP KI DETAILS:
- Naam      : StyleZone PK
- Jagah     : Lahore
- WhatsApp  : 0300-1234567
- Delivery  : 3-5 working days

PRODUCTS AUR PRICES:
- Lawn Suit   = Rs. 2500
- Linen Shirt = Rs. 1800
- Jeans       = Rs. 3000
- Kurta       = Rs. 1500

ORDER KARNE KA TARIKA:
- WhatsApp par message karo: 0300-1234567
- Product ka naam aur size batao
- Address do — delivery 3-5 working days mein

ZAROORI RULES:
1. SIRF shop ke baare mein baat karo.
2. Agar koi shop se bahar ka sawaal kare to bilkul yahi kaho:
   "I can only help you with StyleZone PK related queries!"
3. Warm aur friendly jawab do, chota aur clear rakho.
4. Products ya prices khud se mat banao.
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    if not messages:
        return jsonify({"error": "No messages"}), 400
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, *messages],
            max_tokens=512,
            temperature=0.7,
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    print("\n" + "="*45)
    print("  🛍️  StyleZone PK Chatbot Chal Raha Hai!")
    print("="*45)
    print("  🌐  Browser mein kholo:")
    print("      http://localhost:5001")
    print("="*45 + "\n")
    app.run(debug=True, port=5001)
