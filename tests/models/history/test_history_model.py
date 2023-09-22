import json
from src.models.history_model import HistoryModel


def test_request_history():
    testes_json = HistoryModel.list_as_json()
    tests = json.loads(testes_json)

    assert len(tests) == 2
    assert tests[0]["text_to_translate"] == "I drink water in the morning"
    assert tests[0]["translate_from"] == "en"
    assert tests[0]["translate_to"] == "pt"
