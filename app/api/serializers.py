from rest_framework.serializers import ModelSerializer

from accounts.models import ServiceStation
from autohistory.models import Car
from rest_framework import serializers
from comments_and_rating.models import ServiceStationRating


class CarStorySerializer(ModelSerializer):
    service_station = serializers.CharField(source='service_station_name.station_name')

    class Meta:
        model = Car
        fields = [
            'id',
            'vin_code',
            'mileage',
            'mileage_units',
            'mileage_photo',
            'damage',
            'check_number',
            'service_station_name',
            'service_station',
            'damage',
            'work',
        ]


class ServiceStationSerializer(ModelSerializer):
    class Meta:
        model = ServiceStation
        fields = [
            'station_name',
            'city',
            'address',
            'phone',
            'email',
            'station_avatar',
        ]


class ServiceStationRatingSerializer(ModelSerializer):
    service_station_id = serializers.CharField(source='service_station.id')
    service_station_name = serializers.CharField(source='service_station.station_name')

    class Meta:
        model = ServiceStationRating
        fields = [
            'service_station_id',
            'service_station_name',
            'rating',

        ]

