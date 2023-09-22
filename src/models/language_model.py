from .abstract_model import AbstractModel
from database.db import db


# Requisito 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict = {}):
        super().__init__(data)

    # Requisito 2
    def to_dict(self):
        return {"name": self.data["name"], "acronym": self.data["acronym"]}

    # Requisito 3
    @classmethod
    def list_dicts(cls):
        data = cls.find()
        if not data:
            return []
        list_data = [item.to_dict() for item in data]
        return list_data
