from django.urls import path
from api import views

app_name = 'api'


urlpatterns = [
    path('car/stories/<vin_code>/', views.CarStoryListView.as_view(), name='car_stories'),
    path('service-station/details/<pk>/', views.ServiceStationDetailsView.as_view(), name='service_station_details'),
    path('service-station/rating/list/', views.ServiceStationRatingListView.as_view(),
         name='service_station_rating_list')
    ]
