from django.views import generic
from comments_and_rating.models import CommentsAndRatings, ServiceStationRating
from comments_and_rating.forms import CommentsAndRatingsForm
from autohistory.models import Car
from django.urls import reverse_lazy
from django_filters.views import FilterView
from comments_and_rating.filters import ServiceStationsFilter


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


class ServiceStationsRatingListView(FilterView):
    queryset = ServiceStationRating.objects.select_related('service_station').all()
    template_name = 'service_stations_rating_list.html'
    paginate_by = 2
    filterset_class = ServiceStationsFilter

    def get_context_data(self, *args, object_list=None, **kwargs):
        context: dict = super().get_context_data(*args, **kwargs)
        filters_params = self.request.GET.copy()
        if self.page_kwarg in filters_params:
            del filters_params[self.page_kwarg]

        context['filter_params'] = filters_params.urlencode()
        return context

