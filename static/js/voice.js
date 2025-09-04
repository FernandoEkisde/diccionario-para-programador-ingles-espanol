// Enhanced Voice recognition and synthesis for web with improved UX

class VoiceAssistant {
    constructor() {
        this.isListening = false;
        this.isSpeaking = false;
        this.recognition = null;
        this.currentLang = 'es-ES'; // Default to Spanish
        this.init();
    }

    async init() {
        await this.loadLanguageFromServer();
        this.setupSpeechSynthesis();
        this.setupSpeechRecognition();
        this.bindEvents();
    }

    async loadLanguageFromServer() {
        try {
            const response = await fetch('/api/idioma');
            const data = await response.json();
            this.currentLang = data.lang_code;
        } catch (error) {
            console.error('Error loading language from server:', error);
            // Fallback to Spanish
            this.currentLang = 'es-ES';
        }
    }

    setupSpeechSynthesis() {
        if ('speechSynthesis' in window) {
            // Configure speech synthesis
            speechSynthesis.onvoiceschanged = () => {
                const voices = speechSynthesis.getVoices();
                // Try to find a Spanish voice, fallback to default
                const spanishVoice = voices.find(voice => voice.lang.startsWith('es'));
                if (spanishVoice) {
                    this.voice = spanishVoice;
                }
            };
        }
    }

    setupSpeechRecognition() {
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            this.recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = this.currentLang;
            this.recognition.maxAlternatives = 1;

            this.recognition.onstart = () => {
                this.updateButtonState('listening');
                this.addMessage('🎤 Escuchando...', 'system');
            };

            this.recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                console.log('Heard: ' + transcript);
                this.handleTranscript(transcript);
            };

            this.recognition.onerror = (event) => {
                console.error('Speech recognition error:', event.error);
                this.handleError(event.error);
            };

            this.recognition.onend = () => {
                this.updateButtonState('idle');
                this.isListening = false;
            };
        }
    }

    bindEvents() {
        const voiceBtn = document.getElementById('voice-btn');
        const chatOutput = document.getElementById('chat-output');

        if (voiceBtn) {
            voiceBtn.addEventListener('click', () => {
                if (!this.isListening) {
                    this.startListening();
                } else {
                    this.stopListening();
                }
            });
        }
    }

    startListening() {
        if (this.recognition && !this.isListening) {
            try {
                this.recognition.lang = this.currentLang;
                this.recognition.start();
                this.isListening = true;
            } catch (error) {
                console.error('Error starting recognition:', error);
                this.addMessage('❌ Error al iniciar el reconocimiento de voz.', 'error');
            }
        } else {
            this.addMessage('❌ El reconocimiento de voz no está disponible en este navegador.', 'error');
        }
    }

    stopListening() {
        if (this.recognition && this.isListening) {
            this.recognition.stop();
        }
    }

    handleTranscript(transcript) {
        // Display what was heard
        this.addMessage(`👤 ${transcript}`, 'user');

        // Process the transcript to find the word
        const word = transcript.trim().toLowerCase();
        this.searchWord(word);
    }

    async searchWord(word) {
        try {
            this.addMessage('🔍 Buscando definición...', 'system');

            const response = await fetch('/api/definicion/' + encodeURIComponent(word));
            const data = await response.json();

            if (data.encontrada) {
                const responseText = `📖 <strong>${data.palabra}:</strong> ${data.definicion}<br><em>Traducción: ${data.traduccion}</em>`;
                this.addMessage(responseText, 'bot');
                this.speak(data.definicion);
            } else {
                this.addMessage(`❌ ${data.mensaje}`, 'error');
                this.speak(data.mensaje);
            }
        } catch (error) {
            console.error('Error fetching definition:', error);
            const errorMsg = '❌ Error al obtener la definición. Inténtalo de nuevo.';
            this.addMessage(errorMsg, 'error');
            this.speak('Error al obtener la definición');
        }
    }

    speak(text) {
        if ('speechSynthesis' in window && !this.isSpeaking) {
            this.isSpeaking = true;
            const utterance = new SpeechSynthesisUtterance(text);

            if (this.voice) {
                utterance.voice = this.voice;
            }

            utterance.rate = 0.9;
            utterance.pitch = 1;
            utterance.volume = 0.8;

            utterance.onend = () => {
                this.isSpeaking = false;
            };

            utterance.onerror = (event) => {
                console.error('Speech synthesis error:', event.error);
                this.isSpeaking = false;
            };

            speechSynthesis.speak(utterance);
        } else if (this.isSpeaking) {
            // If already speaking, wait and try again
            setTimeout(() => this.speak(text), 100);
        } else {
            this.addMessage('❌ La síntesis de voz no está disponible en este navegador.', 'error');
        }
    }

    handleError(error) {
        let message = '❌ Error en el reconocimiento de voz.';
        switch (error) {
            case 'no-speech':
                message = '❌ No se detectó habla. Inténtalo de nuevo.';
                break;
            case 'audio-capture':
                message = '❌ Error de captura de audio. Verifica los permisos del micrófono.';
                break;
            case 'not-allowed':
                message = '❌ Acceso al micrófono denegado. Permite el acceso e inténtalo de nuevo.';
                break;
            case 'network':
                message = '❌ Error de red. Verifica tu conexión a internet.';
                break;
        }
        this.addMessage(message, 'error');
        this.updateButtonState('idle');
    }

    addMessage(text, type = 'bot') {
        const chatOutput = document.getElementById('chat-output');
        if (chatOutput) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message message-${type} p-2 mb-2 rounded`;
            messageDiv.innerHTML = text;

            // Add appropriate styling based on message type
            switch (type) {
                case 'user':
                    messageDiv.classList.add('bg-blue-600', 'text-white');
                    break;
                case 'bot':
                    messageDiv.classList.add('bg-gray-600', 'text-yellow-300');
                    break;
                case 'system':
                    messageDiv.classList.add('bg-yellow-600', 'text-black', 'font-semibold');
                    break;
                case 'error':
                    messageDiv.classList.add('bg-red-600', 'text-white');
                    break;
            }

            chatOutput.appendChild(messageDiv);
            chatOutput.scrollTop = chatOutput.scrollHeight;
        }
    }

    updateButtonState(state) {
        const voiceBtn = document.getElementById('voice-btn');
        if (voiceBtn) {
            voiceBtn.classList.remove('bg-blue-600', 'bg-yellow-500', 'bg-red-600', 'animate-pulse');

            switch (state) {
                case 'listening':
                    voiceBtn.classList.add('bg-red-600', 'animate-pulse');
                    voiceBtn.innerHTML = '🎤 Escuchando...';
                    break;
                case 'idle':
                    voiceBtn.classList.add('bg-blue-600');
                    voiceBtn.innerHTML = '🎙️ Hablar';
                    break;
            }
        }
    }

    // Method to change language
    setLanguage(lang) {
        this.currentLang = lang;
        if (this.recognition) {
            this.recognition.lang = lang;
        }
    }
}

// Initialize voice assistant when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.voiceAssistant = new VoiceAssistant();
});
