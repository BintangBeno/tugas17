from flask import Flask, jsonify

app = Flask(__name__)

recipes = [
    {"id": 1, "name": "Nasi Goreng", "ingredients": ["Nasi", "Telur", "Kecap", "Bawang"]},
    {"id": 2, "name": "Mie Goreng", "ingredients": ["Mie", "Sayur", "Kecap", "Bawang"]},
    {"id": 3, "name": "Ayam Bakar", "ingredients": ["Ayam", "Kecap", "Bumbu Bakar"]}
]

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    return jsonify({"recipes": recipes})

if __name__ == '__main__':
    app.run(debug=True)
