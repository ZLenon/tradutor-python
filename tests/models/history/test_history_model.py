import json
from src.models.history_model import HistoryModel


def test_request_history():
    json_tests = HistoryModel.list_as_json()
    tests = json.loads(json_tests)

    assert len(tests) == 2
    assert tests[0]["text_to_translate"] == "do you like bubble gum?"
    assert tests[0]["translate_from"] == "en"
    assert tests[0]["translate_to"] == "pt"
