from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    historico = HistoryModel(
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    UserModel({"name": "Admin", "token": "token"}).save()

    usuario = UserModel.find_one({"name": "Admin"})

    res_post = app_test.delete(
        f"/admin/history/{historico.data['_id']}",
        headers={
            "Authorization": usuario.data["token"],
            "User": usuario.data["name"],
        },
    )

    status_ok = 200
    assert res_post.status_code == status_ok

    cache = HistoryModel.find_one({"_id": historico.data["_id"]})
    assert cache is None
