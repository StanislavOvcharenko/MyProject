from django.shortcuts import render
from django.views import generic
from accounts.forms import SignUpForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.models import ServiceStation
from accounts.forms import ProfileForm, ServiceStationForm


class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')


class ProfileView(generic.UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class ServiceStationCreateView(generic.CreateView):
    model = ServiceStation
    form_class = ServiceStationForm
    template_name = 'create_service_station.html'
    success_url = reverse_lazy('autohistory:create_auto_history')

    def get_form_kwargs(self):
        instance = super().get_form_kwargs()
        instance['initial'] = {'company': self.request.user}
        return instance
