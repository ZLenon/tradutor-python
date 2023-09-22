import json
from src.models.history_model import HistoryModel

# =================MOCK====================================
mock_traducao = [
    {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    },
    {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    },
]


# ===============TEST=========================================
def test_request_history(prepare_base):
    historico_string = json.loads(HistoryModel.list_as_json())

    for x in historico_string:
        x.pop("_id")

    assert historico_string == mock_traducao
    assert len(historico_string) == 2
    assert (
        historico_string[0]["text_to_translate"] == "Hello, I like videogame"
    )
    assert historico_string[0]["translate_from"] == "en"
    assert historico_string[0]["translate_to"] == "pt"
