from django import forms
from autohistory.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'vin_code',
            'mileage_units',
            'mileage',
            'service_station_name',
            'damage',
            'work',
            'check_number',
        )
        labels = {

            'vin_code': 'Він-код',
            'mileage_units': 'Одиниці виміру',
            'mileage': 'Пробіг',
            'service_station_name': 'Назва СТО',
            'damage': 'Пошкодження',
            'work': 'Роботи',
            'check_number': 'Фіскальний номер чека',

        }


class SearchCarHistoryForm(forms.Form):
    vin = forms.CharField(max_length=20)
