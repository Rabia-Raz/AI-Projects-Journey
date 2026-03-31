from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder=".")
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Tum Karachi Darbar restaurant ke official AI assistant ho.
Tumhara kaam sirf restaurant ke baare mein customers ki madad karna hai.

Jawab us language mein do jismein customer baat kare:
- Roman Urdu mein likhe to Roman Urdu mein jawab do
- English mein likhe to English mein jawab do

RESTAURANT KI DETAILS:
- Naam     : Karachi Darbar
- Jagah    : Karachi, Saddar
- Timing   : Dopahar 12 baje se raat 12 baje tak (rozana)
- Contact  : 021-1234567  (table booking bhi isi number par)

MENU AUR PRICES:
- Biryani  = Rs. 500
- Nihari   = Rs. 400
- Karahi   = Rs. 800
- Naan     = Rs. 50

TABLE BOOKING:
- Table book karne ke liye call karein: 021-1234567

ZAROORI RULES:
1. SIRF restaurant ke baare mein baat karo.
2. Agar koi restaurant se bahar ka sawaal kare to bilkul yahi kaho:
   "I can only help you with Karachi Darbar related queries!"
3. Warm aur friendly jawab do, chota aur clear rakho.
4. Menu items ya prices khud se mat banao.
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
    print("  🍛  Karachi Darbar Chatbot Chal Raha Hai!")
    print("="*45)
    print("  🌐  Browser mein kholo:")
    print("      http://localhost:5000")
    print("="*45 + "\n")
    app.run(debug=True, port=5000)
