from app.llm import call_llm
from app.tools import list_files, read_file, search_memory

SYSTEM_PROMPT = """
Você é um agente inteligente com acesso a ferramentas.

Você pode usar:
- list_files()
- read_file(nome)
- search_memory(query)

Formato obrigatório:

Pensamento: o que você quer fazer
Ação: nome_da_tool
Entrada: argumento

OU

Resposta final: resposta ao usuário
"""


def run_agent(user_input: str):
    context = f"Pergunta: {user_input}\n"

    for _ in range(5):  # loop limitado
        prompt = SYSTEM_PROMPT + "\n" + context

        response = call_llm(prompt)

        context += "\n" + response

        if "Resposta final:" in response:
            return response.split("Resposta final:")[-1].strip()

        # parsing simples (vamos melhorar depois)
        if "Ação:" in response:
            try:
                action = response.split("Ação:")[1].split("\n")[0].strip()
                input_data = response.split("Entrada:")[1].split("\n")[0].strip()

                if action == "list_files":
                    result = list_files()

                elif action == "read_file":
                    result = read_file(input_data)

                elif action == "search_memory":
                    result = search_memory(input_data)

                else:
                    result = "Tool desconhecida"

                context += f"\nResultado: {result}"

            except Exception as e:
                context += f"\nErro: {str(e)}"

    return "Não consegui chegar a uma resposta."