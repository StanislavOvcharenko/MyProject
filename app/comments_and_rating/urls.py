from django.urls import path
from comments_and_rating import views

app_name = 'comments_and_rating'


urlpatterns = [
    path('create/comments_and_rating/<str:check_number>', views.CommentAndRatingCreateView.as_view(),
         name='create_comments_and_rating'),
    # path('create/comments_and_rating/', views.CommentAndRatingCreateView.as_view(),
    #      name='create_comments_and_rating'),
    ]