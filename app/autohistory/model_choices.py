from django.db import models


class MileageUnitType(models.TextChoices):
    UNIT_TYPE_KILOMETER = 'Км', 'Кілометр'
    UNIT_TYPE_MILES = 'Мі', 'Мілі'
