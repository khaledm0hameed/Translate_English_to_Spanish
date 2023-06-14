from googletrans import Translator

def translate_spanish_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='es', dest='en')
    return translation.text

# Example usage
spanish_text = input("Enter u word ::  ")
english_text = translate_spanish_to_english(spanish_text)
print(english_text)
