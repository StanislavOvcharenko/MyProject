from django import forms

from accounts.models import ServiceStation
from autohistory.models import CarStory


class CarForm(forms.ModelForm):
    damage_photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False,
                                   label=("Завантажте фотографіх пошкоджень"))
    email = forms.EmailField(label="Введіть пошту кліета")

    class Meta:
        model = CarStory
        fields = (
            'vin_code',
            'mileage_units',
            'mileage',
            'mileage_photo',
            'service_station_name',
            'damage',
            'work',
            'check_number',
        )
        labels = {

            'vin_code': 'Він-код',
            'mileage_units': 'Одиниці виміру',
            'mileage': 'Пробіг',
            'mileage_photo': 'Завантажте фото одометру',
            'service_station_name': 'Назва СТО',
            'damage': 'Пошкодження',
            'work': 'Роботи',
            'check_number': 'Фіскальний номер чека',

        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs['initial']['company']
        super().__init__(*args, **kwargs)
        self.fields['service_station_name'].queryset = ServiceStation.objects.filter(company=user_id)


class SearchCarHistoryForm(forms.Form):
    vin = forms.CharField(max_length=17, min_length=17)
