from googletrans import Translator


def get_translated(text, from_lang='en', to_lang='uk'):
    translator = Translator()
    result = translator.translate(text, src=from_lang, dest=to_lang)
    return result.text


