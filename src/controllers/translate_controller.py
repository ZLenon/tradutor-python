from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from models.history_model import HistoryModel
from deep_translator import GoogleTranslator


translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index():
    dialeto = LanguageModel.list_dicts()
    if request.method == "POST":
        texto = request.form.get("text-to-translate")
        do = request.form.get("translate-from")
        para = request.form.get("translate-to")
        traduzido = GoogleTranslator(source=do, target=para).translate(texto)
        historico = HistoryModel(
            {
                "text_to_translate": texto,
                "translate_from": do,
                "translate_to": para,
            }
        )
        historico.save()

        return render_template(
            "index.html",
            text_to_translate=texto,
            translated=traduzido,
            languages=dialeto,
            translate_from=do,
            translate_to=para,
        )

    if request.method == "GET":
        return render_template(
            "index.html",
            languages=dialeto,
            text_to_translate="what's your name?",
            translate_from="en",
            translate_to="pt",
            translated="Tradução",
        )


@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    dialeto = LanguageModel.list_dicts()
    texto = request.form.get("text-to-translate")
    do = request.form.get("translate-from")
    para = request.form.get("translate-to")
    traduzido = GoogleTranslator(source=do, target=para).translate(texto)
    HistoryModel(
        {
            "text_to_translate": texto,
            "translate_from": do,
            "translate_to": para,
        }
    ).save()

    return render_template(
        "index.html",
        text_to_translate=traduzido,
        translate_from=para,
        languages=dialeto,
        translated=texto,
        translate_to=do,
    )
