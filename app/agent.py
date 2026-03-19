from app.llm import call_llm
from app.settings import get_settings
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


def _truncate_llm_prompt(context: str) -> str:
    settings = get_settings()
    system = SYSTEM_PROMPT
    overhead = len(system) + len("\n")
    max_ctx = max(512, settings.agent_max_prompt_chars - overhead)
    if len(context) <= max_ctx:
        return system + "\n" + context
    marker = "\n...[contexto anterior omitido por limite de tamanho]...\n"
    keep = max_ctx - len(marker)
    if keep < 512:
        keep = 512
    tail = context[-keep:]
    return system + marker + tail


def run_agent(user_input: str):
    context = f"Pergunta: {user_input}\n"

    for _ in range(5):  # loop limitado
        prompt = _truncate_llm_prompt(context)

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
