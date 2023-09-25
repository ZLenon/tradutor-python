from src.models.history_model import HistoryModel
from src.models.user_model import UserModel

# ===============MOCK==============================
mock_traducao = {
    "text_to_translate": "I drink water in the morning",
    "translate_from": "en",
    "translate_to": "pt",
}
login = {"name": "lenon", "token": "string-do-token-jwt"}
name = {"name": "lenon"}
status_ok = 204


# ===============TEST==============================
def test_history_delete(app_test):
    historico = HistoryModel(mock_traducao).save()

    UserModel(login).save()

    usuario = UserModel.find_one(name)

    res_post = app_test.delete(
        f"/admin/history/{historico.data['_id']}",
        headers={
            "Authorization": usuario.data["token"],
            "User": usuario.data["name"],
        },
    )

    assert res_post.status_code == status_ok

    dell = HistoryModel.find_one({"_id": historico.data["_id"]})
    assert dell is None
