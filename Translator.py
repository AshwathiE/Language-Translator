import googletrans

translator = googletrans.Translator()

print(googletrans.LANGUAGES)

translated = translator.translate('How are you', 
                     dest = 'hi')

print(translated.text)