import uuid

from django import forms
from django.contrib.auth import get_user_model
from accounts.models import ServiceStation
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from autohistory.tasks import send_activate_mail


class SignUpForm(forms.ModelForm):
    password_confirmation = forms.CharField(label='Підтвердження пароля')

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password',
        ]
        labels = {'email': 'Пошта',
                  'password': 'Пароль',
                  }

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password_confirmation']:
                raise forms.ValidationError("Паролі не співпадають")

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = str(uuid.uuid4())
        instance.is_active = False
        instance.set_password(self.cleaned_data['password'])

        if commit:
            instance.save()

        send_activate_mail.delay(instance.username, instance.email)

        return instance


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'EDRPOU',
            'company_name'
        ]
        labels = {
            'EDRPOU': 'ЄДРПОУ',
            'company_name': 'Назва команії'
        }


class ServiceStationForm(forms.ModelForm):
    class Meta:
        model = ServiceStation
        fields = [
            'station_name',
            'city',
            'address',
            'phone',
            'email',
            'station_avatar',
            'company'
        ]
        labels = {
            'station_name': 'Назва станції',
            'city': 'Місто',
            'address': 'Адреса',
            'phone': 'Номер телефону',
            'email': 'Пошта',
            'station_avatar': 'Завантажте фото станції'
        }
        widgets = {'company': forms.HiddenInput()}

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.company = self.initial['company']
        if commit:
            instance.save()
        return instance


class ServiceStationUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceStation
        fields = [
            'station_name',
            'city',
            'address',
            'phone',
            'email',
            'station_avatar'
        ]
        labels = {
            'station_name': 'Назва станції',
            'city': 'Місто',
            'address': 'Адреса',
            'phone': 'Номер телефону',
            'email': 'Пошта',
            'station_avatar': 'Змінити фото станції'
        }
