from flask import Blueprint, request, jsonify
import deepl
from src.config import DEEPL_API_KEY

from parrot import Parrot
import warnings

warnings.filterwarnings("ignore")

rephrase = Blueprint(name="rephrase", import_name=__name__, url_prefix="/paraphrase")
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")
translator = deepl.Translator(DEEPL_API_KEY)


def split_sentences(text: str):
    return [sentence.strip() for sentence in text.split(".")]


def paraphrase(parrot, phrases):
    para_phrases = parrot.augment(phrases, max_return_phrases=10, do_diverse=True)
    max_score = 0
    paraphrased = para_phrases[0][0]
    for para_phrase in para_phrases:
        score = para_phrase[-1]
        if score > max_score:
            max_score = score
            paraphrased = para_phrase[0]
    return paraphrased


@rephrase.route("/", methods=["POST"])
def paraphrase_text():
    phrase = request.form["text"]
    phrase = phrase.replace('"', "'")
    result = translator.translate_text(phrase, target_lang="EN-US")

    # paraphrase
    sentences = []
    for translated in split_sentences(result.text)[:-1]:
        sentences.append(paraphrase(parrot, translated))

    # translate back to whatever the source language is
    src_lang_text = translator.translate_text(
        '. '.join(sentences), target_lang=result.detected_source_lang
    )

    return jsonify({'paraphrased': src_lang_text.text})


if __name__ == "__main__":
    # parrot = Parrot()
    phrase = input("Masukan frasa: ")
    phrase = phrase.replace('"', "'")
    phrases = split_sentences(phrase)[:-1]
    result = translator.translate_text(phrase, target_lang="EN-US")
    for translated in split_sentences(result.text)[:-1]:
        print("---")
        print(paraphrase(parrot, translated.text))
        print(translated)
        print("---")
