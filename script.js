const chatLog = document.getElementById('chat-log');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const message = userInput.value.trim();
    if (message) {
        displayMessage('user', message);
        // Aqui você fará a chamada para a sua API Python/Gemini
        getResponse(message);
        userInput.value = '';
    }
}

function displayMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(`${sender}-message`);
    messageDiv.textContent = message;
    chatLog.appendChild(messageDiv);
    chatLog.scrollTop = chatLog.scrollHeight; // Manter a última mensagem visível
}

async function getResponse(userMessage) {
    try {
        const response = await fetch('http://127.0.0.1:5000/pergunta', { // Endereço da sua API Flask (padrão)
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ pergunta: userMessage })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        displayMessage('chatbot', data.resposta);

    } catch (error) {
        console.error('Erro ao obter resposta:', error);
        displayMessage('chatbot', 'Desculpe, houve um erro ao processar sua pergunta.');
    }
}

function generateChatbotResponse(userMessage) {
    // Aqui você implementará a lógica para gerar respostas baseadas na sua bio
    // Esta é uma versão simplificada
    if (userMessage.toLowerCase().includes('nome')) {
        return "Meu nome é um chatbot pessoal baseado nas informações de Salvador Yuran Mário.";
    } else if (userMessage.toLowerCase().includes('idade')) {
        return "Salvador tem 21 anos.";
    } else if (userMessage.toLowerCase().includes('hobby')) {
        return "O hobby principal de Salvador é videojogos.";
    } else if (userMessage.toLowerCase().includes('filme favorito')) {
        return "Os top 3 filmes favoritos de Salvador são Batman Cavaleiro das Trevas, Fight Club e HARD TARGET.";
    } else if (userMessage.toLowerCase().includes('comida favorita')) {
        return "As comidas favoritas de Salvador são Pizza, Shawarmas e Burguers.";
    } else if (userMessage.toLowerCase().includes('sonho')) {
        return "Um dos sonhos de Salvador é viajar mundo fora.";
    } else {
        return "Interessante! Conte-me mais sobre o que você gostaria de saber.";
    }
}