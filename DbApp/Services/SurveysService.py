from DbApp import models
from DbApp.Services import VehiclePinService, IssueService
import datetime


def get_surveys(date: str, user_name: str = None, vehicle_plate: str = None) -> list:
    """Получить Surveys"""
    surveys = models.Survey.objects().select_related()
    border_date = _convert_to_date(date)
    surveys = filter(lambda x: _convert_to_date(x.date) >= border_date, surveys)
    if vehicle_plate is not None: # фильтрация по номеру
        surveys = filter(lambda x: x.vehicle.plate == vehicle_plate, surveys)
    output = [] # содержит survey
    if user_name is not None: # фильтрация по имени
        for s in surveys:
            names = [s.name for s in VehiclePinService.get_users(s.vehicle)]
            if user_name in names:
                output.append(s)
    else:
        output = list(surveys)
    for s in output:
        s.users.append(VehiclePinService.get_users(s.vehicle))
        s.issues.append(IssueService.get_issues_by_vehicle(s.vehicle))
    output.sort(key=lambda s: _convert_to_date(s.date), reverse=True)
    return output


def _convert_to_date(date: str) -> datetime:
    """Конвертировать строку в datetime"""
    return datetime.datetime.strptime(date, '%d-%m-%Y')






