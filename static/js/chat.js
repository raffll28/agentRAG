(function () {
  const chat = document.getElementById("chat");
  const form = document.getElementById("form");
  const input = document.getElementById("input");
  const sendBtn = document.getElementById("send");

  function appendMessage(role, text, isError) {
    const el = document.createElement("div");
    el.className = "msg " + (isError ? "error" : role);
    el.textContent = text;
    chat.appendChild(el);
    chat.scrollTop = chat.scrollHeight;
  }

  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    const q = input.value.trim();
    if (!q) return;

    appendMessage("user", q);
    input.value = "";
    sendBtn.disabled = true;

    try {
      const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ q }),
      });
      const data = await res.json().catch(function () {
        return {};
      });
      if (!res.ok) {
        appendMessage(
          "bot",
          data.detail ? String(data.detail) : "Erro HTTP " + res.status,
          true
        );
        return;
      }
      appendMessage("bot", data.response != null ? String(data.response) : "(sem resposta)");
    } catch (err) {
      appendMessage("bot", "Falha de rede: " + err.message, true);
    } finally {
      sendBtn.disabled = false;
      input.focus();
    }
  });

  appendMessage(
    "bot",
    "Olá. Envie uma pergunta; o agente pode consultar arquivos em app/memory/ e responder via Ollama."
  );
  input.focus();
})();
