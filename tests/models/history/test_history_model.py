import json
from src.models.history_model import HistoryModel


def test_request_history():
    historico_json = HistoryModel.list_as_json()
    historico_string = json.loads(historico_json)

    for x in historico_string:
        x.pop("_id")

    mock_traducao = [
        {
            "text_to_translate": "i drink water in the morning",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "I study often",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]

    assert historico_string == mock_traducao
