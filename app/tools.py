import os

MEMORY_PATH = "app/memory"


def list_files():
    return os.listdir(MEMORY_PATH)


def read_file(filename: str):
    path = os.path.join(MEMORY_PATH, filename)
    if not os.path.exists(path):
        return "Arquivo não encontrado"

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def search_memory(query: str):
    results = []

    for file in os.listdir(MEMORY_PATH):
        content = read_file(file)

        if query.lower() in content.lower():
            results.append(f"Arquivo: {file}\n{content}")

    return "\n\n".join(results) if results else "Nada encontrado"