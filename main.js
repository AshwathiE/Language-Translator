document.addEventListener('DOMContentLoaded', () => {

    const textarea = document.querySelector('textarea');
    const translateButton = document.querySelector('.translate-btn');

    // Translate button validation
    translateButton.addEventListener('click', (event) => {

        if (textarea.value.trim() === '') {
            event.preventDefault();
            alert('Please enter text to translate');
        }
    });

});

// Speech Recognition Function
function startSpeechRecognition() {

    const recognition = new webkitSpeechRecognition();

    recognition.lang = 'en-US';

    recognition.onresult = function(event) {

        const transcript = event.results[0][0].transcript;

        document.querySelector('textarea').value = transcript;
    };

    recognition.start();
}