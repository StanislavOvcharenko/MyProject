from celery import shared_task
from comments_and_rating.models import ServiceStationRating, CommentsAndRatings
from autohistory.models import ServiceStation


@shared_task
def update_service_stations_rating():
    for station in ServiceStation.objects.all():
        count = 0
        balls = 0
        for rating in CommentsAndRatings.objects.select_related('car_working').filter(
              car_working__service_station_name=station.id):
            balls += rating.rating
            count += 1
        if count > 0:
            rating_obj = ServiceStationRating.objects.get_or_create(service_station=station)
            rating_obj[0].rating = balls/count
            rating_obj[0].save()
