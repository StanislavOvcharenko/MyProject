from django.db import models
from autohistory.model_choices import MileageUnitType
from accounts.models import ServiceStation


class Car(models.Model):
    vin_code = models.CharField(max_length=20)
    mileage_units = models.CharField(max_length=2, choices=MileageUnitType.choices)
    mileage = models.IntegerField()
    service_station_name = models.ForeignKey('accounts.ServiceStation', on_delete=models.DO_NOTHING)
    damage = models.TextField(max_length=1000)
    work = models.TextField(max_length=10000)
    check_number = models.CharField(max_length=22)
    created = models.DateField(auto_now_add=True)
