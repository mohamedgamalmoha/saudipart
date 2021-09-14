from django.urls import path
from .views import HowWorksView


app_name = 'info'

urlpatterns = [
    path('detail/', HowWorksView.as_view(), name='detail')
]
