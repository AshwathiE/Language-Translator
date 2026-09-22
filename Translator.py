import googletrans

translator = googletrans.Translator()

print(googletrans.LANGUAGES)

language = input("Enter language code: ")

if language not in googletrans.LANGUAGES:
    print("Invalid language code")
else:
    translated = translator.translate(
        "How are you",
        dest=language
    )

    print(translated.text)