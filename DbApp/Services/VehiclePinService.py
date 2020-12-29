from DbApp import models
from DbApp.Services import UserService, VehicleService


def get_users(vehicle: models.Vehicle) -> list:
    """Получить users по vehicle"""
    vp = models.VehiclePin.objects(vehicle=vehicle.id.__str__())
    output = []
    for i in vp:
        output.append(UserService.get_user_by_id(i.user))
    return output


def get_vehicles(user: models.User) -> list:
    """Получить vehicles по user"""
    vp = models.VehiclePin.objects(user=user.id.__str__())
    output = []
    for i in vp:
        output.append(VehicleService.get_vehicle_by_id(i.vehicle))
    return output
