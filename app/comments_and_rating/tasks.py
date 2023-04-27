from accounts.models import ServiceStation
from autohistory.models import Car
from comments_and_rating.models import CommentsAndRatings, ServiceStationRating


def service_station_rating_create():
    queryset = CommentsAndRatings.objects.select_related('car')
    return queryset

a = service_station_rating_create()