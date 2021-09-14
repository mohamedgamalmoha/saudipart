import csv

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models.aggregates import Sum
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, TemplateView

from .models import Robbery
from .forms import RobberyForm
from accounts.decorators import AuthUser, AuthAdmin


class HomeView(TemplateView):
    template_name = 'home.html'


class RobberyView(AuthUser, SuccessMessageMixin, CreateView):
    model = Robbery
    form_class = RobberyForm
    template_name = 'robbery/robbery_add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('robbery:home')
    success_message = 'تم اضافة المعلومات بنجاح'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RobberyListView(AuthUser, ListView):
    model = Robbery
    paginate_by = 10
    template_name = 'robbery/robbery_list.html'
    context_object_name = 'obj_lst'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).values('gang_iban').distinct()


class RobberyListViewAdmin(AuthAdmin, ListView):
    model = Robbery
    queryset = model.objects.values('gang_iban').distinct()
    paginate_by = 10
    template_name = 'robbery/robbery_list.html'
    context_object_name = 'obj_lst'


def get_robbery(request, iban):
    objects = Robbery.objects.filter(gang_iban=iban)
    user = request.user
    if user.is_authenticated and not user.is_superuser:
        objects.filter(user=user)
    return objects


def robbery_profile(request, iban):
    objects = get_robbery(request, iban)
    total_embezzled_amount = objects.aggregate(Sum('embezzled_amount')).get('embezzled_amount__sum')
    context = {'objects': objects, 'total': total_embezzled_amount, 'count': objects.count()}
    return render(request, 'robbery/robbery_profile.html', context)


def export_csv(request, iban):
    objects = get_robbery(request, iban)
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['اسم الضحية', 'رقم البطاقه الوطنيه', 'رقم جوال', 'المبلغ الذي تمت سرقته', 'هل تم التحويل للخارج مباشره', 'اي بي الوسيط'])
    for member in objects.values_list('victim_name', 'victim_national_id', 'victim_phone_number',  'embezzled_amount', 'outboard_transferred', 'mediator_iban'):
        writer.writerow(member)
    response['Content-Disposition'] = f'attachment; filename="{objects.first().gang_iban}.csv"'
    return response
