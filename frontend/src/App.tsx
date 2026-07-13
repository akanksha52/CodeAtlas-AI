import { useState } from "react";
import { sendMessage } from "./services/chatService";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  async function handleSend() {
    if (!message.trim()) return;

    const data = await sendMessage(message);
    setResponse(data.response);
  }

  return (
    <main>
      <h1>AI Code Intelligence Platform</h1>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={handleSend}>
        Send
      </button>

      <p>{response}</p>
    </main>
  );
}

export default App;