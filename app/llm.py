import os

import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = os.environ.get("OLLAMA_MODEL", "qwen3.5:9b")
REQUEST_TIMEOUT_SEC = float(os.environ.get("OLLAMA_TIMEOUT", "120"))


def call_llm(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
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
