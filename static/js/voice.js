// Voice recognition and synthesis for web

function speak(text) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        window.speechSynthesis.speak(utterance);
    } else {
        alert('Speech synthesis not supported in this browser.');
    }
}

function listen(callback) {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'es-ES'; // Change to 'en-US' if needed
        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            console.log('Heard: ' + transcript);
            callback(transcript);
        };
        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
        };
        recognition.start();
    } else {
        alert('Speech recognition not supported in this browser.');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const voiceBtn = document.getElementById('voice-btn');
    const chatOutput = document.getElementById('chat-output');

    if (voiceBtn) {
        voiceBtn.addEventListener('click', function() {
            listen(function(transcript) {
                // Display what was heard
                chatOutput.innerHTML += '<p><strong>Tú:</strong> ' + transcript + '</p>';

                // Process the transcript to find the word
                const word = transcript.trim().toLowerCase();
                fetch('/api/definicion/' + encodeURIComponent(word))
                    .then(response => response.json())
                    .then(data => {
                        if (data.encontrada) {
                            const responseText = '<strong>' + data.palabra + ':</strong> ' + data.definicion + ' (' + data.traduccion + ')';
                            chatOutput.innerHTML += '<p><strong>Bot:</strong> ' + responseText + '</p>';
                            speak(data.definicion);
                        } else {
                            chatOutput.innerHTML += '<p><strong>Bot:</strong> ' + data.mensaje + '</p>';
                            speak(data.mensaje);
                        }
                        // Scroll to bottom
                        chatOutput.scrollTop = chatOutput.scrollHeight;
                    })
                    .catch(error => {
                        console.error('Error fetching definition:', error);
                        chatOutput.innerHTML += '<p><strong>Bot:</strong> Error al obtener la definición.</p>';
                    });
            });
        });
    }
});
