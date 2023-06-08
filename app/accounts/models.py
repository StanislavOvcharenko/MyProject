from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


def station_avatar(instance, filename):
    data = datetime.datetime.now()
    return 'station_avatar/{}/{}/{}/{}/{}/{}'.format(data.year, data.month, data.day,
                                                     instance.station_name, instance.company.id, filename)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField("email address", unique=True)
    EDRPOU = models.IntegerField(unique=True, null=True, default=None)
    company_name = models.CharField(max_length=120, null=True, default=None)


class ServiceStation(models.Model):
    station_name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    station_avatar = models.ImageField(upload_to=station_avatar,
                                       default='accounts/images/default_station_photo.jpeg', null=True)
    company = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.station_name
