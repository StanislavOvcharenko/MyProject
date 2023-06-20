from django.db import models
from autohistory.model_choices import MileageUnitType
from accounts.models import ServiceStation
import datetime


def photo_mileage(instance, filename):
    data = datetime.datetime.now()
    return 'mileage_photo/{}/{}/{}/{}/{}/{}'.format(data.year, data.month, data.day, instance.vin_code,
                                                       instance.service_station_name.station_name, filename)


def photo_damages(instance, filename):
    data = datetime.datetime.now()
    return 'damages_photo/{}/{}/{}/{}/{}/{}'.format(data.year, data.month, data.day, instance.car_story.vin_code,
                                                       instance.car_story.service_station_name.station_name, filename)


class CarStory(models.Model):
    vin_code = models.CharField(max_length=17)
    mileage_units = models.CharField(max_length=2, choices=MileageUnitType.choices)
    mileage = models.IntegerField()
    mileage_photo = models.ImageField(upload_to=photo_mileage, null=True)
    service_station_name = models.ForeignKey('accounts.ServiceStation', on_delete=models.DO_NOTHING)
    damage = models.TextField(max_length=1000)
    work = models.TextField(max_length=10000)
    check_number = models.CharField(max_length=22)
    created = models.DateField(auto_now_add=True)


class DamagePhoto(models.Model):
    car_story = models.ForeignKey('CarStory', on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to=photo_damages, null=True, blank=True)
