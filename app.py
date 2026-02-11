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
    # Optional session id to keep separate conversations. If not provided,
    # use a default global session.
    session_id = data.get("session_id", "default")
    try:
        # If the client provided a `messages` array, use it (client-side history).
        # Expected format: [{"role": "user"|"assistant", "text": "..."}, ...]
        client_messages = data.get("messages")

        if client_messages and isinstance(client_messages, list):
            recent = client_messages[-15:]
            convo_lines = []
            for m in recent:
                role = m.get("role")
                text = m.get("text", "")
                label = "User" if role == "user" else "Assistant"
                convo_lines.append(f"{label}: {text}")
            prompt_for_model = "\n".join(convo_lines) + "\nAssistant:"
        else:
            # Fallback: single-turn prompt
            prompt_for_model = f"User: {prompt}\nAssistant:"

        result = generate(model="gemma3:4b", prompt=prompt_for_model)
        response_text = result.response

        # Return the assistant response and echo back the recent messages (client can append the assistant reply)
        if client_messages and isinstance(client_messages, list):
            recent_messages = client_messages[-15:]
        else:
            recent_messages = [{"role": "user", "text": prompt}]
        recent_messages.append({"role": "assistant", "text": response_text})
        recent_messages = recent_messages[-15:]

        return jsonify({"response": response_text, "session_id": session_id, "recent_messages": recent_messages})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Error communicating with Ollama"}), 500

if __name__ == "__main__":
    app.run(debug=True)
