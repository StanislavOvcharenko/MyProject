from django.urls import path
from autohistory import views

app_name = 'autohistory'


urlpatterns = [
    path('create/autohistory/', views.CarStoryCreateHistoryView.as_view(), name='create_auto_history'),
    path('details/<int:pk>/', views.CarStoryHistoryDetailView.as_view(), name='history_details'),
    path('car-story/list/<str:pk>/', views.CarStoriesListView.as_view(), name='car_story'),
    # path('details/car-story/service-station/<str:pk>/', views.CarStoryServiceStationsDataView.as_view(),
    #      name='car_story_service_station_details'),
    path('damage/photos/<int:pk>/', views.CarDamagePhotosListView.as_view(), name='damage_photos'),
    ]
