# Define a dictionary with English words and their translations
languages = {
    "Spanish": {
        "hello": "hola",
        "goodbye": "adiós",
        "water": "agua",
    },
    "French": {
        "hello": "bonjour",
        "goodbye": "au revoir",
        "water": "eau",
    },
}


def translate_word(english_word, target_language):
    """
    This function translates an English word to the target language.

    Args:
        english_word: The English word to translate.
        target_language: The language to translate to (e.g., "Spanish", "French").

    Returns:
        The translated word in the target language,
        or "Word not found" if not available.
    """
    # Check if the target language is available
    if target_language not in languages:
        return "Language not supported"

    # Get the translation dictionary for the target language
    translation_dict = languages[target_language]

    # Check if the word exists in the dictionary
    if english_word.lower() in translation_dict:
        return translation_dict[english_word.lower()]
    else:
        return "Word not found"


# Get user input for target language
target_language = input(
    "Enter the language to translate to (Spanish, French): "
).capitalize()

# Get user input for the word to translate
english_word = input("Enter the word you want to translate: ")

# Translate the word and display the result
translated_word = translate_word(english_word, target_language)
print(f"{english_word} in {target_language} is: {translated_word}")
