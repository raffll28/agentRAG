import os

import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
REQUEST_TIMEOUT_SEC = float(os.environ.get("OLLAMA_TIMEOUT", "120"))


def call_llm(prompt: str) -> str:
    model = (os.environ.get("OLLAMA_MODEL") or "").strip()
    if not model:
        return (
            "Erro: OLLAMA_MODEL não está definido. Copie .env.example para .env "
            "e defina OLLAMA_MODEL com o nome exato do modelo no Ollama (veja `ollama list`)."
        )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=REQUEST_TIMEOUT_SEC,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return f"Erro ao chamar o LLM: {e}"

    text = data.get("response")
    if text is None:
        return f"Resposta do LLM sem campo 'response': {data!r}"
    return text
