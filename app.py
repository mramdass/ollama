from flask import Flask, render_template, request, jsonify
from ollama import generate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    prompt = data["prompt"]
    
    try:
        result = generate(model="gemma3:4b", prompt=prompt)  # Or your Ollama model name
        return jsonify({"response": result.response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Error communicating with Ollama"}), 500

if __name__ == "__main__":
    app.run(debug=True)
