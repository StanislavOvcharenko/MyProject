from django.urls import path, include
from accounts import views

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create/service-station/', views.ServiceStationCreateView.as_view(), name='create_service_station'),
    ]
