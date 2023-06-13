import django_filters
from comments_and_rating.models import ServiceStationRating


class ServiceStationsFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='service_station__city', label='Місто')
    station_name = django_filters.CharFilter(field_name='service_station__station_name', label='Назва Станції')

    class Meta:
        model = ServiceStationRating
        fields = ['city', 'station_name']
