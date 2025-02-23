import { useState, useEffect, useRef } from "react";
import { Send } from "lucide-react";
import "./Chatbot.css";

export default function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null); // Referencia para el scroll automático

  const handleSend = async () => {
    if (input.trim() === "") return;

    const userMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();
      const botMessage = { text: data.response, sender: "bot" };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("Error al conectar con el backend:", error);
      setMessages((prev) => [...prev, { text: "Error en el servidor", sender: "bot" }]);
    }
  };

  // Efecto para hacer scroll automático cuando cambien los mensajes
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="container">
      <div className="chat-section">
        <div className="chat-header">Chatbot - Energias Renovables</div>
        <div className="chat-messages">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.sender === "user" ? "user-message" : "bot-message"}`}
            >
              {msg.text}
            </div>
          ))}
          {/* Elemento invisible para anclar el scroll */}
          <div ref={chatEndRef}></div>
        </div>
        <div className="chat-input-container">
          <input
            type="text"
            className="chat-input"
            placeholder="Escribe tu mensaje..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === "Enter" && handleSend()}
          />
          <button className="send-button" onClick={handleSend}>
            <Send size={20} />
          </button>
        </div>
      </div>

      <div className="info-section">
        <div className="resources-section">
          <h3>Recursos sobre Energias Renovables</h3>
          <ul>
            <li><a href="https://www.irena.org/" target="_blank" rel="noopener noreferrer">Agencia Internacional de Energias Renovables (IRENA)</a></li>
            <li><a href="https://www.un.org/es/climatechange" target="_blank" rel="noopener noreferrer">Naciones Unidas - Cambio Climatico</a></li>
            <li><a href="https://www.iea.org/" target="_blank" rel="noopener noreferrer">Agencia Internacional de Energia (IEA)</a></li>
            <li><a href="https://climate.nasa.gov/" target="_blank" rel="noopener noreferrer">NASA - Cambio Climatico</a></li>
          </ul>
        </div>

        <div className="faq-section">
          <h3>Preguntas Frecuentes</h3>
          <ul>
            <li>¿Que son las energias renovables?</li>
            <li>¿Como contribuyen las energias renovables al medio ambiente?</li>
            <li>¿Que tipos de energia renovable existen?</li>
            <li>¿Cuales son los desafios actuales en la implementacion de energias renovables?</li>
          </ul>
        </div>
      </div>
    </div>
  );
}
