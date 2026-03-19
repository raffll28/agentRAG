from app.llm import call_llm
from app.tools import default_tool_usage_block, run_tool

SYSTEM_PROMPT = f"""
Você é um agente inteligente com acesso a ferramentas.

Você pode usar:
{default_tool_usage_block()}

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

        if "Ação:" in response:
            try:
                action = response.split("Ação:")[1].split("\n")[0].strip()
                input_data = response.split("Entrada:")[1].split("\n")[0].strip()

                result = run_tool(action, input_data)
                context += f"\nResultado: {result}"

            except Exception as e:
                context += f"\nErro: {str(e)}"

    return "Não consegui chegar a uma resposta."
