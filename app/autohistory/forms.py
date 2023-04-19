from django import forms

from accounts.models import ServiceStation
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

    def __init__(self, *args, **kwargs):
        user_id = kwargs['initial']['company']
        super().__init__(*args, **kwargs)
        self.fields['service_station_name'].queryset = ServiceStation.objects.filter(company=user_id)

        '''Create choices for field service_station_name '''

        company_choices = [(company.id, company.station_name) for company in ServiceStation.objects.filter(
            company=user_id)]
        self.fields['service_station_name'].choices = company_choices




class SearchCarHistoryForm(forms.Form):
    vin = forms.CharField(max_length=20)
