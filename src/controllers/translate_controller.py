from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index():
    available_languages = LanguageModel.list_dicts()

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        source_language = request.form.get("source-language")
        target_language = request.form.get("target-language")

        translated_text = GoogleTranslator(
            source=source_language, target=target_language
        ).translate(text_to_translate)

        return render_template(
            "index.html",
            available_languages=available_languages,
            input_text=text_to_translate,
            source_language=source_language,
            target_language=target_language,
            translated_text=translated_text,
        )
    else:
        translated_text = "Tradução"

    return render_template(
        "index.html",
        available_languages=available_languages,
        translated_text=translated_text,
    )


@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    available_languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    source_language = request.form.get("source-language")
    target_language = request.form.get("target-language")

    # Troca as linguagens de origem e destino
    source_language, target_language = target_language, source_language

    translator = GoogleTranslator(
        source="auto", target=source_language
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        available_languages=available_languages,
        input_text=text_to_translate,
        source_language=source_language,
        target_language=target_language,
        translated_text=translator,
    )
