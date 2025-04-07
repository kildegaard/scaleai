from googletrans import Translator

# Initialize the translator
translator = Translator()


# Function to translate Spanish to English
def translate(spanish_sentence):
    # Translate the sentence
    translated = translator.translate(spanish_sentence, src="es", dest="en")
    return translated.text


if __name__ == "__main__":
    spanish_sentence = "Hola, cómo estás? Buenos días!"
    english_sentence = translate(spanish_sentence)
    print(f"Spanish: {spanish_sentence}")
    print(f"English: {english_sentence}")
