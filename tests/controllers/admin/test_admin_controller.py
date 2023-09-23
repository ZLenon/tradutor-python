from src.models.history_model import HistoryModel
from src.models.user_model import UserModel

# ================MOCK=============================
mock_traducao = {
    "text_to_translate": "Hello, I like videogame",
    "translate_from": "en",
    "translate_to": "pt",
}
usuario_mock = {"name": "usuario123", "token": "abcdwzas454646"}


# ================TEST=============================
def test_history_delete(app_test):
    history = HistoryModel(mock_traducao).save()

    UserModel(usuario_mock).save()

    um_usuario = UserModel.find_one({"name": "usuario123"})

    res_post = app_test.delete(
        f"/admin/history/{history.data['_id']}",
        headers={
            "Authorization": um_usuario.data["abcdwzas454646"],
            "User": um_usuario.data["name"],
        },
    )

    assert res_post.status_code == 204
    assert HistoryModel.find_one({"_id": history.data["_id"]}) is None
