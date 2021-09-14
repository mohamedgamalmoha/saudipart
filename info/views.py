from django.views.generic import TemplateView

from .models import HowWorks


class HowWorksView(TemplateView):
    template_name = 'info/detail.html'

    def get_context_data(self, **kwargs):
        context = super(HowWorksView, self).get_context_data(**kwargs)
        context['obj'] = HowWorks.objects.first()
        return context
