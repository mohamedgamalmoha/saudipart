from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .models import Thief, Victim
from .forms import ThiefForm, VictimForm


class HomeView(TemplateView):
    template_name = 'home.html'


class ThiefView(SuccessMessageMixin, CreateView):
    model = Thief
    form_class = ThiefForm
    template_name = 'thief/thief.html'
    context_object_name = 'form'
    success_message = 'Thief info has added successfully'

    def get_success_url(self):
        obj = self.get_object()
        return reverse('thief:thief_profile', args=[obj.id, ])


class VictimView(SuccessMessageMixin, CreateView):
    model = Victim
    form_class = VictimForm
    template_name = 'thief/victim.html'
    context_object_name = 'form'
    success_message = 'Victim info has added successfully'

    def get_success_url(self):
        return reverse('thief:thief_profile', args=[self.object.thief.id, ])


class ThiefDetailView(DetailView):
    model = Thief
    template_name = 'thief/thief_profile.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_lst'] = Victim.objects.filter(thief=self.get_object()).distinct()
        return context


class ThiefListView(ListView):
    model = Thief
    paginate_by = 10
    template_name = 'thief/thief_list.html'
    context_object_name = 'obj_lst'
    ordering = 'name'
