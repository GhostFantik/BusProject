from DbApp import models


def get_issues_by_vehicle(vehicle: models.Vehicle) -> list:
    issues = models.Issue.objects().select_related()
    output = filter(lambda x: x.vehicle == vehicle, issues)
    return list(output)
