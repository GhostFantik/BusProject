from DbApp import models


def get_user_by_id(_id: str) -> models.User:
    """Получить юзера по id"""
    return models.User.objects.get(id=_id)