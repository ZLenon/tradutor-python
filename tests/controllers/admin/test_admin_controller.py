from src.models.history_model import HistoryModel
from src.models.user_model import UserModel

# ================MOCK=================================
mock_traducao = {
    "text_to_translate": "Hello, I like videogame",
    "translate_from": "en",
    "translate_to": "pt",
}
mock_usuario = {"name": "Admin", "token": "coxina_123"}
mock_name = {"name": "Admin"}
status_ok = 204


# ===============TEST===================================
def test_history_delete(path_url):
    h = HistoryModel(mock_traducao).save()
    UserModel(mock_usuario).save()
    um_usuario = UserModel.find_one(mock_name)

    r = path_url.delete(
        f"/admin/history/{h.data['_id']}",
        headers={
            "Authorization": um_usuario.data["coxina_123"],
            "User": um_usuario.data["name"],
        },
    )

    assert r.status_code == status_ok
    dell = HistoryModel.find_one({"_id": h.data["_id"]})
    assert dell is None
