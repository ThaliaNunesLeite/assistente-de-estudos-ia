"""
Assistente de Estudos IA - Backend (Flask)

Funcionalidades:
- Recebe pergunta do usuário (/api/ask)
- Seleciona a versão mais recente do prompt (prompt_v*.txt)
- Chama a API da OpenAI (ou outra) se API key estiver configurada
- Salva logs das interações em logs/interactions.json
- Endpoints: / (frontend), /api/ask (POST)
- Modo "mock" (sem API) para desenvolvimento local

Como usar (resumo):
1) instalar dependências: pip install -r requirements.txt
2) export OPENAI_API_KEY="sua_chave_aqui" (opcional; funciona em mock sem chave)
3) python app.py
"""

import os
import json
import glob
from datetime import datetime
from flask import Flask, request, jsonify, render_template
try:
    import openai
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

BASE_DIR = os.path.dirname(__file__)
LOG_PATH = os.path.join(BASE_DIR, "logs", "interactions.json")

app = Flask(__name__)

def load_latest_prompt():
    """Load the latest prompt_v*.txt by filename order (v1, v2, v3...)"""
    pattern = os.path.join(BASE_DIR, "prompt_v*.txt")
    files = sorted(glob.glob(pattern))
    if not files:
        return "You are an Assistant."
    with open(files[-1], "r", encoding="utf-8") as f:
        return f.read().strip()

def save_log(entry):
    os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
    if not os.path.exists(LOG_PATH):
        data = []
    else:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception:
                data = []
    data.append(entry)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def call_llm(prompt, question, max_tokens=400):
    """
    Calls the OpenAI API (if available and key set) otherwise returns a simple mock response.
    The system prompt and the user question are combined to build the final input.

    Requires environment variable OPENAI_API_KEY if using real API.
    """
    final_input = prompt + "\n\nPergunta: " + question
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY_OPENAI")
    if OPENAI_AVAILABLE and api_key:
        try:
            openai.api_key = api_key
            # Using ChatCompletion style for compatibility
            response = openai.ChatCompletion.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini") ,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": question}
                ],
                max_tokens=max_tokens,
                temperature=0.2,
            )
            text = response["choices"][0]["message"]["content"].strip()
            return {"text": text, "meta": {"provider":"openai", "usage": response.get("usage") }}
        except Exception as e:
            # Fall back to mock
            return {"text": f"[MOCK] Erro ao chamar API: {e}\nResposta mock para: {question}", "meta":{"provider":"mock"}}
    else:
        # Mocked simple assistant for local dev (no API key)
        mock = f"[MOCK] Assistente de Estudos - Resposta simples para: {question}\n\nExplicação: ...\nExemplo: ...\nExercício: ..."
        return {"text": mock, "meta":{"provider":"mock"}}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error":"Pergunta vazia"}), 400
    prompt = load_latest_prompt()
    result = call_llm(prompt, question)
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "question": question,
        "prompt_used": prompt.splitlines()[0] if prompt else "",
        "response": result["text"],
        "meta": result.get("meta", {})
    }
    save_log(entry)
    return jsonify(entry)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
