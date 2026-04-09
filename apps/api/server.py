from flask import Flask, request, jsonify
from pathlib import Path

app = Flask(__name__)

PROMPT_PATH = Path(__file__).resolve().parents[2] / "configs" / "prompts" / "system-builder.md"

def load_system_prompt() -> str:
    try:
        return PROMPT_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return "You are the 3dvr Builder Assistant."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    system_prompt = load_system_prompt()

    if not message:
        return jsonify({"error": "Missing message"}), 400

    reply = (
        f"{system_prompt}\n\n"
        f"User goal: {message}\n\n"
        "Starter response:\n"
        "- Pick one simple offer\n"
        "- Make a one-page landing page\n"
        "- Add one clear contact method\n"
        "- Launch fast and improve from feedback"
    )
    return jsonify({"reply": reply})

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
