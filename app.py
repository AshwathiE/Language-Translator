from flask import Flask, render_template, request
import googletrans
from gtts import gTTS
import os

app = Flask(__name__)

translator = googletrans.Translator()
languages = googletrans.LANGUAGES

@app.route('/', methods=['GET', 'POST'])
def home():

    translated_text = ""
    audio_file = None

    if request.method == 'POST':

        text = request.form['text']
        dest_language = request.form['language']

        # Translate text
        translated = translator.translate(text, dest=dest_language)

        translated_text = translated.text

        # Convert translated text to speech
        tts = gTTS(
            text=translated_text,
            lang=dest_language
        )

        # Save audio
        audio_path = "static/output.mp3"

        tts.save(audio_path)

        audio_file = audio_path

    return render_template(
        'index.html',
        languages=languages,
        translated_text=translated_text,
        audio_file=audio_file
    )

if __name__ == '__main__':
    app.run(debug=True)