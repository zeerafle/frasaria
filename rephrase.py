from flask import Blueprint, jsonify, make_response
from deep_translator import GoogleTranslator, single_detection
import config
from parrot import Parrot
import warnings
warnings.filterwarnings("ignore")

def detect_language(phrase: str):
    return single_detection(phrase, api_key=config.DETECT_LANG_API)

def translate(texts, source, target='en'):
    return GoogleTranslator(source=source, target=target).translate_batch(texts)

def split_sentences(text: str):
    return [sentence.strip() for sentence in text.split('.')]

def paraphrase(parrot, phrases):
    # TODO: figure out how to run this line once
    para_phrases = parrot.augment(phrases, max_return_phrases=10)
    max_score = 0
    paraphrased = para_phrases[0][0]
    for para_phrase in para_phrases:
        score = para_phrase[-1]
        if score > max_score:
            max_score = score
            paraphrased = para_phrase[0]
    return paraphrased

if __name__ == '__main__':
    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")
    # parrot = Parrot()
    phrase = input('Masukan frasa: ')
    phrase = phrase.replace('"', "'")
    phrases = split_sentences(phrase)[:-1]
    lang = detect_language(phrases[0])
    if lang in ['id', 'ms']:
        translated_texts = translate(phrases, 'id')
    for translated_text in translated_texts:
        print('---')
        print(paraphrase(parrot, translated_text))
        print(translated_text)
        print('---')

