from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .forms import RegistrationForm


class LogInView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('robbery:home')
    redirect_authenticated_user = True
    success_message = 'تم نسجيل الدخول'


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_message = 'تم ادخال البيانات بطريقة صحيحة'
    success_url = reverse_lazy('robbery:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class LogOutView(SuccessMessageMixin, LogoutView):
    template_name = 'accounts/logout.html'
    success_message = 'تم نسجيل الخروج'
