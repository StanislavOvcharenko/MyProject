import uuid

from django import forms
from django.contrib.auth import get_user_model
from accounts.models import ServiceStation
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

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
        instance.set_password(self.cleaned_data['password'])

        if commit:
            instance.save()

        self._send_activation_email()

        return instance

    def _send_activation_email(self):
        subject = 'Activate account'
        message = f'''
        Activation link: {settings.HTTP_SCHEMA}://{settings.DOMAIN}{reverse('accounts:activate',
                                                                            args=(self.instance.username,))}'''

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [self.instance.email],
            fail_silently=False,
        )


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
            'company'
        ]
        labels = {
            'station_name': 'Назва станції',
            'city': 'Місто',
            'address': 'Адреса',
            'phone': 'Номер телефону',
            'email': 'Пошта'
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
        ]
        labels = {
            'station_name': 'Назва станції',
            'city': 'Місто',
            'address': 'Адреса',
            'phone': 'Номер телефону',
            'email': 'Пошта'
        }
