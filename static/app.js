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
        color: white;
        text-align: center;
        margin-top: 40vh;
        font-family: Arial, sans-serif;
      ">
        Uce is Offline
      </h1>;
  }

