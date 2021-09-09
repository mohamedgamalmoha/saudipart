from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.db.models.aggregates import Sum
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, TemplateView

from .models import Robbery
from .forms import RobberyForm

import csv


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
    queryset = model.objects.raw('SELECT gang_ip, id FROM thief_robbery GROUP BY gang_ip')
    paginate_by = 1
    template_name = 'robbery/robbery_list.html'
    context_object_name = 'obj_lst'


def robbery_profile(request, ip):
    objects = Robbery.objects.filter(gang_ip=ip)
    total = objects.aggregate(Sum('embezzled_amount')).get('embezzled_amount__sum')
    context = {'objects': objects, 'total': total}
    return render(request, 'robbery/robbery_profile.html', context)


def export_csv(request, ip):
    objects = Robbery.objects.filter(gang_ip=ip)
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['اسم الضحية', 'رقم البطاقه الوطنيه', 'رقم جوال', 'المبلغ الذي تمت سرقته', 'هل تم التحويل للخارج مباشره', 'اي بي الوسيط'])
    for member in objects.values_list('victim_name', 'victim_national_id', 'victim_phone_number',  'embezzled_amount', 'outboard_transferred', 'mediator_ip'):
        writer.writerow(member)
    response['Content-Disposition'] = f'attachment; filename="{objects.first().gang_ip}.csv"'
    return response
