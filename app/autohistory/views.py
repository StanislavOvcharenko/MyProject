from autohistory.models import CarStory, DamagePhoto
from autohistory.forms import CarForm, SearchCarHistoryForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from accounts.models import ServiceStation
from autohistory.tasks import send_link_for_comment


class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = SearchCarHistoryForm

    def form_valid(self, form):
        vin = form.cleaned_data.get('vin')
        self.success_url = reverse('autohistory:auto', kwargs={'pk': vin})
        return super().form_valid(form)


class CarStoriesListView(generic.ListView):
    template_name = 'my_auto_history.html'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        vin_code = self.kwargs['pk']
        queryset = CarStory.objects.filter(vin_code=vin_code).order_by('-created').all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vin_code'] = self.kwargs['pk']
        return context


class CarStoryCreateHistoryView(generic.CreateView):
    queryset = CarStory.objects.all()
    template_name = 'create_auto_history.html'
    form_class = CarForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        instance = super().get_form_kwargs()
        instance['initial'] = {'company': self.request.user.id}
        return instance

    def form_valid(self, form):

        car = form.save()

        send_link_for_comment.delay(form.cleaned_data['check_number'], form.cleaned_data['email'])

        damage_photos = self.request.FILES.getlist('damage_photo')
        for photo in damage_photos:
            DamagePhoto.objects.create(photo=photo, car_story=car)
        return super().form_valid(form)


class CarStoryHistoryDetailView(generic.DetailView):
    queryset = CarStory.objects.select_related('commentsandratings').all()
    template_name = 'auto_history_details.html'


class CarStoryServiceStationsDataView(generic.DetailView):
    queryset = ServiceStation.objects.all()
    template_name = 'car_story_services_stations.html'


class CarDamagePhotosListView(generic.ListView):
    queryset = DamagePhoto.objects.all()
    template_name = 'damage_photos.html'

    def get_queryset(self):
        car_story_id = self.kwargs['pk']
        queryset = DamagePhoto.objects.filter(car_story=car_story_id).all()
        return queryset
