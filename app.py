from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# 🔑 PUT YOUR API KEY HERE
API_KEY = "YOUR_OPENROUTER_API_KEY"

# ⚡ Faster free models
MODEL_A = "openchat/openchat-7b:free"
MODEL_B = "nvidia/nemotron-3-super-120b-a12b:free"

def ask_ai(model, messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8080",
        "X-Title": "AI Debate App"
    }

    data = {
        "model": model,
        "messages": messages,
        "max_tokens": 150
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=10  # 🔥 HARD LIMIT
        )

        print("Status:", response.status_code)
        print("Response:", response.text[:200])  # debug

        if response.status_code != 200:
            return f"⚠️ API Error: {response.text}"

        json_data = response.json()

        return json_data['choices'][0]['message']['content']

    except requests.exceptions.Timeout:
        return "⚠️ Timeout: AI too slow."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask_individual', methods=['POST'])
def ask_individual():
    data = request.json
    model = data.get('model_id')
    history = data.get('history', [])

    print("Model used:", model)  # debug

    reply = ask_ai(model, history)
    return jsonify({"reply": reply})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
