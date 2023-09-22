import json
from src.models.history_model import HistoryModel

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


def test_request_history(prepare_base):
    historico_string = json.loads(HistoryModel.list_as_json())

    for x in historico_string:
        x.pop("_id")

    assert historico_string == mock_traducao
