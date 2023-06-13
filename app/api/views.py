from rest_framework import generics
from autohistory.models import CarStory
from api.serializers import CarStorySerializer, ServiceStationSerializer, ServiceStationRatingSerializer
from accounts.models import ServiceStation
from comments_and_rating.models import ServiceStationRating


class CarStoryListView(generics.ListAPIView):
    queryset = CarStory.objects.select_related('service_station_name').all()
    serializer_class = CarStorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(vin_code=self.kwargs['vin_code']).all()
        return queryset


class ServiceStationDetailsView(generics.RetrieveAPIView):
    queryset = ServiceStation.objects.all()
    serializer_class = ServiceStationSerializer


class ServiceStationRatingListView(generics.ListAPIView):
    queryset = ServiceStationRating.objects.select_related('service_station').all()
    serializer_class = ServiceStationRatingSerializer
