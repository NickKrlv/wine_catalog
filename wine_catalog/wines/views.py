from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .forms import ContactForm
from .models import Wine


class WineListView(ListView):
    model = Wine
    template_name = 'wines/wine_list.html'
    context_object_name = 'wine_list'


class WineDetailView(DetailView):
    model = Wine
    template_name = 'wines/wine_detail.html'
    context_object_name = 'wine'


class ContactView(FormView):
    template_name = 'wines/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        # Здесь можно добавить логику отправки email или сохранения сообщения в базу данных
        return super().form_valid(form)
