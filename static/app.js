const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const log = document.getElementById("chat-log");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, "user");
  input.value = "";

  const typing = addMessage("Typing...");

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text })
  });

  const data = await res.json();
  typing.remove();
  addMessage(data.reply, "bot");
});

function addMessage(text, type) {
  const div = document.createElement("div");
  div.className = `message ${type}`;
  div.textContent = text;
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
  return div;
}

  const PAUSED = true;
  if (PAUSED) {
    document.body.innerHTML = 
      <h1 style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background: #000;
        color: white;
        font-family: system-ui, sans-serif;
        font-size: 2rem;
      ">
        Uce is Offline
      </h1>;
  }


