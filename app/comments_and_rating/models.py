from django.db import models


class CommentsAndRatings(models.Model):
    comment_text = models.CharField(max_length=1000)
    rating = models.IntegerField()
    car_working = models.OneToOneField('autohistory.Car', on_delete=models.DO_NOTHING, blank=True, null=True)


