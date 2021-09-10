import csv

from django.http import HttpResponse
from django.db.models.aggregates import Sum
from django.shortcuts import render, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, TemplateView

from .models import Robbery
from .forms import RobberyForm


class HomeView(TemplateView):
    template_name = 'home.html'


class RobberyView(SuccessMessageMixin, CreateView):
    model = Robbery
    form_class = RobberyForm
    template_name = 'robbery/robbery_add.html'
    context_object_name = 'form'
    success_message = 'تم اضافة المعلومات بنجاح'

    def get_success_url(self):
        return reverse('robbery:home')


class RobberyListView(ListView):
    model = Robbery
    queryset = model.objects.values('gang_iban').distinct()
    paginate_by = 10
    template_name = 'robbery/robbery_list.html'
    context_object_name = 'obj_lst'


def robbery_profile(request, iban):
    objects = Robbery.objects.filter(gang_iban=iban)
    total_embezzled_amount = objects.aggregate(Sum('embezzled_amount')).get('embezzled_amount__sum')
    context = {'objects': objects, 'total': total_embezzled_amount, 'count': objects.count()}
    return render(request, 'robbery/robbery_profile.html', context)


def export_csv(request, iban):
    objects = Robbery.objects.filter(gang_iban=iban)
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['اسم الضحية', 'رقم البطاقه الوطنيه', 'رقم جوال', 'المبلغ الذي تمت سرقته', 'هل تم التحويل للخارج مباشره', 'اي بي الوسيط'])
    for member in objects.values_list('victim_name', 'victim_national_id', 'victim_phone_number',  'embezzled_amount', 'outboard_transferred', 'mediator_iban'):
        writer.writerow(member)
    response['Content-Disposition'] = f'attachment; filename="{objects.first().gang_iban}.csv"'
    return response
