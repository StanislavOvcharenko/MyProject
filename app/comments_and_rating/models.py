from django.db import models


class CommentsAndRatings(models.Model):
    comment_text = models.CharField(max_length=1000)
    rating = models.IntegerField()
    car_working = models.OneToOneField('autohistory.Car', on_delete=models.DO_NOTHING, blank=True, null=True)


class ServiceStationRating(models.Model):
    service_station = models.OneToOneField('accounts.ServiceStation', on_delete=models.DateField)
    rating = models.DecimalField(max_digits=5, decimal_places=3, null=True)

# for station in ServiceStation.objects.all():
#     count = 0
#     balls = 0
#     for rating in CommentsAndRatings.objects.select_related('car_working').filter(
#           car_working__service_station_name=station.id):
#         balls += rating.rating
#         count += 1
#     if count > 0:
#         rating_obj = ServiceStationRating.objects.get_or_create(service_station=station)
#         rating_obj[0].rating = balls/count
#         rating_obj[0].save()
