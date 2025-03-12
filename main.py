from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    {"author": "Albert Einstein", "quote": "Life is like riding a bicycle. To keep your balance you must keep moving."},
    {"author": "Steve Jobs", "quote": "Stay hungry, stay foolish."},
    {"author": "Nelson Mandela", "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
    {"author": "Confucius", "quote": "It does not matter how slowly you go as long as you do not stop."},
    {"author": "Oprah Winfrey", "quote": "Turn your wounds into wisdom."}
]

@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify(random.choice(quotes))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
