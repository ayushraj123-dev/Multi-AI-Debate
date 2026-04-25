# 🔥 AI Debate Arena

A futuristic multi-AI debate platform where multiple AI models debate a topic in real time, challenge each other’s arguments, and a final AI Judge decides the winner.

Built using **Flask + HTML/CSS + JavaScript + OpenRouter API**.

---

# 🚀 Features

## ✅ 5 AI Debaters + 1 AI Judge

Each AI plays a unique role:

* 😤 Aggressive Critic
* 🚀 Optimistic Futurist
* 🧪 Scientist
* 🧠 Philosopher
* 💰 Economist
* 👑 Final AI Judge

This creates diverse perspectives instead of repetitive answers.

---

## ✅ 3 Debate Rounds

### Round 1 — Opening Argument

Each AI gives its main stance.

### Round 2 — Rebuttal

Each AI attacks or challenges another AI’s argument.

### Round 3 — Final Conclusion

Each AI gives its strongest final statement.

### Final Judgment

The AI Judge analyzes all arguments and selects:

* Strongest argument
* Weakest argument
* Final winner

---

## ✅ Futuristic UI

Includes:

* Glassmorphism design
* Neon cyberpunk theme
* Smooth debate cards
* Premium debate arena feel

Designed to feel like a next-generation AI platform.

---

# 🛠 Tech Stack

## Backend

* Python
* Flask
* Requests
* OpenRouter API

## Frontend

* HTML
* CSS
* JavaScript

## AI Models

Uses multiple free models from OpenRouter.

Examples:

* Google Gemma
* Llama
* Qwen
* Nvidia Nemotron
* OpenAI OSS
* GLM

(Models may change depending on availability and rate limits)

---

# 📂 Project Structure

```text
AI-Debate-Arena/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# ⚙️ Installation

## Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/AI-Debate-Arena.git
cd AI-Debate-Arena
```

---

## Step 2 — Install Requirements

```bash
pip install flask requests
```

or

```bash
pip install -r requirements.txt
```

---

## Step 3 — Add Your OpenRouter API Key

Open `app.py` and replace:

```python
API_KEY = "your_api_key_here"
```

with your actual OpenRouter API key.

You can get one from:

[https://openrouter.ai/](https://openrouter.ai/)

---

## Step 4 — Run the Project

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:8080
```

---

# ⚠ Common Issues

## 404 Error

This happens when a model ID is invalid.

### Fix:

Use only valid free models from OpenRouter.

---

## 429 Error

This means:

* Rate limit exceeded
* Free daily quota finished
* Model temporarily overloaded

### Fix:

* Wait and retry
* Use different models
* Add credits to OpenRouter for higher limits

---

## CORS Error

This happens when opening `index.html` directly.

### Fix:

Always open through Flask:

```text
http://127.0.0.1:8080
```

Do NOT open with:

```text
file:///...
```

---

# 🎯 Future Upgrades

Planned improvements:

* Debate history saving
* User accounts
* Scoreboard system
* AI personality memory
* Voice debates
* Live streaming debate mode
* Public debate rooms
* Spectator voting
* AI vs Human debate mode
* Tournament system

---

# 💡 Why This Project?

Most AI chat apps are simple Q&A tools.

This project turns AI into:

* debaters
* analysts
* critics
* judges

making conversations far more interesting and useful.

It feels less like a chatbot and more like an AI-powered intellectual arena.

---

# 👨‍💻 Author

Built by Ayush 🚀

Focused on:

* AI
* Startups
* Space Tech
* Future Tech
* Building world-changing systems

---

# ⭐ Support

If you like this project:

* Star the repository
* Fork the project
* Improve it
* Build your own version

Let’s build the future.

---

# License

This project is open-source and free to use for learning and development.
