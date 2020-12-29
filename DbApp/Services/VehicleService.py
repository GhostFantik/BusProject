from DbApp import models


def get_vehicle_by_id(_id: str) -> models.Vehicle:
    """Получить vehicle по id"""
    return models.Vehicle.objects.get(id=_id)