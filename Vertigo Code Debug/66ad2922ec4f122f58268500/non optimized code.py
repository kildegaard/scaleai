spanish_to_english = {
    "hola": "hello",
    "mundo": "world",
    "cómo": "how",
    "estás": "are you",
    "buenos": "good",
    "días": "morning",
    "buenas": "good",
    "tardes": "afternoon",
    "noches": "night",
    "gracias": "thank you",
    "por": "for",
    "favor": "please",
    "sí": "yes",
    "no": "no",
    "perro": "dog",
    "gato": "cat",
}


def translate(spanish_sentence):

    words = spanish_sentence.lower().split()

    translated_words = []
    for word in words:

        clean_word = "".join(e for e in word if e.isalnum())

        if clean_word in spanish_to_english:
            translated_words.append(spanish_to_english[clean_word])
        else:

            translated_words.append(word)

    translated_sentence = " ".join(translated_words)
    return translated_sentence


spanish_sentence = "Hola, cómo estás? Buenos días!"
english_sentence = translate(spanish_sentence)
print(f"Spanish: {spanish_sentence}")
print(f"English: {english_sentence}")
