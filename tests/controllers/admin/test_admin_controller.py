import json
from src.models.history_model import HistoryModel

# from src.models.user_model import UserModel


def test_history_delete(app_test):
    # Verifica se os dados foram inseridos corretamente no banco de dados
    historicos = list(HistoryModel.find_all())
    assert len(historicos) == 2

    # Testa a rota para obter todos os registros de histórico
    res_one = app_test.get("/admin/history")
    assert res_one.status_code == 200
    data_one = json.loads(res_one.data)
    assert len(data_one) == 2

    # Testa a exclusão de um registro de histórico
    res_two = app_test.delete("/admin/history/1")
    assert res_two.status_code == 204
    historico_two = HistoryModel.find_one({"_id": 1})
    assert historico_two is None

    # Testa a atualização de um registro de histórico
    data = {
        "text_to_translate": "Updated text",
        "translate_from": "en",
        "translate_to": "pt",
    }
    res_three = app_test.put("/admin/history/1", data=data)
    assert res_three.status_code == 200
    historico_three = HistoryModel.find_one({"_id": 1})
    assert historico_three["text_to_translate"] == "Updated text"
