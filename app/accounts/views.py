from django.shortcuts import render, get_object_or_404
from django.views import generic
from accounts.forms import SignUpForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.models import ServiceStation
from accounts.forms import ProfileForm, ServiceStationForm, ServiceStationUpdateForm


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


class ServiceStationListView(generic.ListView):
    model = ServiceStation
    template_name = 'list_service_station.html'


class ServiceStationDetailView(generic.DetailView):
    model = ServiceStation
    template_name = 'details_service_station.html'


class ServiceStationUpdateView(generic.UpdateView):
    model = ServiceStation
    form_class = ServiceStationUpdateForm
    template_name = 'update_service_station.html'
    success_url = reverse_lazy('accounts:list_service_station')


class UserActivateView(generic.RedirectView):
    pattern_name = 'index'

    def get(self, request, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_404(get_user_model(), username=username)

        if user.is_active:
            pass
        else:
            user.is_active = True
            user.save()

        response = super().get(request, *args, **kwargs)
        return response
