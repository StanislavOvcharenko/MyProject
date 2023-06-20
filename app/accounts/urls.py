from django.urls import path, include
from accounts import views

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create/service-station/', views.ServiceStationCreateView.as_view(), name='create_service_station'),
    path('list/service-station/', views.ServiceStationListView.as_view(), name='list_service_station'),
    path('details/service-station/<int:pk>/', views.ServiceStationDetailView.as_view(), name='details_service_station'),
    path('update/service-station/<int:pk>/', views.ServiceStationUpdateView.as_view(), name='update_service_station'),
    path('activate/<uuid:username>/', views.UserActivateView.as_view(), name='activate')
    ]
