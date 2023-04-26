from django.views import generic
from comments_and_rating.models import CommentsAndRatings
from comments_and_rating.forms import CommentsAndRatingsForm
from autohistory.models import Car
from django.urls import reverse_lazy


class CommentAndRatingCreateView(generic.CreateView):
    model = CommentsAndRatings.objects.all()
    template_name = 'comments_and_rating_create.html'
    form_class = CommentsAndRatingsForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        instance = super().get_form_kwargs()
        car_story = Car.objects.filter(check_number=self.kwargs['check_number']).last()
        instance['car_story_id'] = car_story.id
        return instance

