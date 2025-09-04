// Voice recognition and synthesis for web
// Note: This is a placeholder for future web-based voice features

function speak(text) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        window.speechSynthesis.speak(utterance);
    } else {
        alert('Speech synthesis not supported in this browser.');
    }
}

function listen() {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'es-ES'; // or 'en-US'
        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            console.log('Heard: ' + transcript);
            // Process the transcript
        };
        recognition.start();
    } else {
        alert('Speech recognition not supported in this browser.');
    }
}

// Example usage
// speak('Hello world');
// listen();
