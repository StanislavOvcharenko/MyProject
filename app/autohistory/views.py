from autohistory.models import Car
from autohistory.forms import CarForm, SearchCarHistoryForm
from django.views import generic
from django.urls import reverse_lazy, reverse


class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = SearchCarHistoryForm

    def form_valid(self, form):
        vin = form.cleaned_data.get('vin')
        self.success_url = reverse('autohistory:auto', kwargs={'pk': vin})
        return super().form_valid(form)


class CarListView(generic.ListView):
    template_name = 'my_auto_history.html'

    def get_queryset(self, **kwargs):
        vin_code = self.kwargs['pk']
        queryset = Car.objects.filter(vin_code=vin_code).all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vin_code'] = self.kwargs['pk']
        return context


class CarCreateHistoryView(generic.CreateView):
    queryset = Car.objects.all()
    template_name = 'create_auto_history.html'
    form_class = CarForm
    success_url = reverse_lazy('index')


class CarHistoryDetailView(generic.DetailView):
    queryset = Car.objects.all()
    template_name = 'auto_history_details.html'


