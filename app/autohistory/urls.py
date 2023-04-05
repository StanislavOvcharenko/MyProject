from django.urls import path
from autohistory import views

app_name = 'autohistory'


urlpatterns = [
    path('create/autohistory/', views.CarCreateHistoryView.as_view(), name='create_auto_history'),
    path('details/<int:pk>', views.CarHistoryDetailView.as_view(), name='history_details'),
    path('auto/<str:pk>/', views.CarListView.as_view(), name='auto'),
    ]
