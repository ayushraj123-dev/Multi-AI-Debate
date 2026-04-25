# =========================================================
# app.py
# AI Debate Arena
# FINAL STABLE SETUP
# ✅ 5 Different AI Personalities
# ✅ 3 Debate Rounds
# ✅ AI Judge
# ✅ Stable Free Models (Less 429 + Less null errors)
# =========================================================

from flask import Flask, render_template, request, jsonify
import requests
import time

app = Flask(__name__)

# =========================================================
# 🔑 YOUR OPENROUTER API KEY
# =========================================================

API_KEY = "YOUR OPENROUTER API KEY"


# =========================================================
# AI PERSONALITIES + MODEL ASSIGNMENT
# =========================================================

AI_PERSONALITIES = [
    {
        "name": "AI 1 - Aggressive Critic 😤",
        "role": "You are an aggressive critic. You focus on dangers, flaws, risks, and worst-case scenarios. You strongly challenge optimistic views.",
        "model": "qwen/qwen3-next-80b-a3b-instruct:free"
    },

    {
        "name": "AI 2 - Optimistic Futurist 🚀",
        "role": "You are an optimistic futurist. You believe technology solves major human problems and creates a better future.",
        "model": "google/gemma-3n-e4b-it:free"
    },

    {
        "name": "AI 3 - Scientist 🧪",
        "role": "You are a scientist. You rely on logic, evidence, facts, research, and rational analysis only.",
        "model": "qwen/qwen-2.5-7b-instruct:free"
    },

    {
        "name": "AI 4 - Philosopher 🧠",
        "role": "You are a philosopher. You focus on ethics, morality, meaning, human values, and long-term consequences.",
        "model": "openai/gpt-oss-20b:free"
    },

    {
        "name": "AI 5 - Economist 💰",
        "role": "You are an economist. You focus on jobs, money, markets, industries, productivity, and financial impact.",
        "model": "mistralai/mistral-7b-instruct:free"
    }
]

# =========================================================
# 👑 JUDGE MODEL
# =========================================================

JUDGE_MODEL = "liquid/lfm-2.5-1.2b-instruct:free"


# =========================================================
# API FUNCTION
# =========================================================

def ask_ai(prompt, model):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8080",
        "X-Title": "AI Debate Arena"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 220,
        "temperature": 0.8
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=45
        )

        # Retry once if rate limited
        if response.status_code == 429:
            print(f"429 Rate Limit on {model}, retrying...")
            time.sleep(3)

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=45
            )

        print(f"MODEL: {model}")
        print(f"STATUS: {response.status_code}")

        if response.status_code != 200:
            return f"⚠ API Error ({response.status_code}): {response.text}"

        result = response.json()

        # Safe response parsing
        if (
            "choices" in result and
            len(result["choices"]) > 0 and
            "message" in result["choices"][0] and
            "content" in result["choices"][0]["message"]
        ):
            content = result["choices"][0]["message"]["content"]

            if content and str(content).strip().lower() != "null":
                return content

        return "⚠ No valid response received from model."

    except Exception as e:
        return f"⚠ System Error: {str(e)}"


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# START DEBATE
# =========================================================

@app.route("/start_debate", methods=["POST"])
def start_debate():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({
            "error": "Please enter a valid debate topic."
        })

    debate_results = []

    # =====================================================
    # ROUND 1 — OPENING ARGUMENT
    # =====================================================

    round_1 = []

    for ai in AI_PERSONALITIES:
        prompt = f"""
{ai['role']}

Debate Topic: {topic}

ROUND 1: Opening Argument

Give your strongest opening argument.

Rules:
- 2 short paragraphs only
- Natural and persuasive
- No templates
- No bullet points
- Strong personality-based response
"""

        reply = ask_ai(prompt, ai["model"])

        round_1.append({
            "name": ai["name"],
            "round": "Round 1 - Opening Argument",
            "reply": reply
        })

    debate_results.extend(round_1)

    # =====================================================
    # ROUND 2 — REBUTTAL
    # =====================================================

    round_2 = []

    for i, ai in enumerate(AI_PERSONALITIES):
        opponent = round_1[(i + 1) % 5]

        prompt = f"""
{ai['role']}

Debate Topic: {topic}

ROUND 2: Rebuttal

Opponent said:

{opponent['reply']}

Rules:
- Strongly disagree
- Counter sharply and logically
- 2 short paragraphs only
- No bullet points
- Stay in character
"""

        reply = ask_ai(prompt, ai["model"])

        round_2.append({
            "name": ai["name"],
            "round": "Round 2 - Rebuttal",
            "reply": reply
        })

    debate_results.extend(round_2)

    # =====================================================
    # ROUND 3 — FINAL CONCLUSION
    # =====================================================

    round_3 = []

    for ai in AI_PERSONALITIES:
        prompt = f"""
{ai['role']}

Debate Topic: {topic}

ROUND 3: Final Conclusion

Give your strongest final conclusion.

Rules:
- Short
- Powerful
- Persuasive
- Convince the audience
- Final statement only
"""

        reply = ask_ai(prompt, ai["model"])

        round_3.append({
            "name": ai["name"],
            "round": "Round 3 - Final Conclusion",
            "reply": reply
        })

    debate_results.extend(round_3)

    # =====================================================
    # 👑 FINAL AI JUDGE
    # =====================================================

    final_summary = ""

    for item in round_3:
        final_summary += f"{item['name']} said:\n{item['reply']}\n\n"

    judge_prompt = f"""
You are the final AI Judge.

Debate Topic: {topic}

Final arguments:

{final_summary}

Your tasks:

1. Identify the strongest argument
2. Identify the weakest argument
3. Choose the final winner
4. Explain clearly why

Rules:
- Be decisive
- Be intelligent
- No vague answers
- Clear final judgment
"""

    judge_reply = ask_ai(judge_prompt, JUDGE_MODEL)

    debate_results.append({
        "name": "👑 AI Judge",
        "round": "Final Judgment",
        "reply": judge_reply
    })

    return jsonify({
        "responses": debate_results
    })


# =========================================================
# RUN APP
# =========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
