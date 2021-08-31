from django.urls import path
from .views import HomeView, ThiefView, VictimView, ThiefDetailView, ThiefListView

app_name = 'thief'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('thief/add', ThiefView.as_view(), name='thief_add'),
    path('victim/add', VictimView.as_view(), name='victim_add'),

    path('thief/list', ThiefListView.as_view(), name='thief_list'),
    path('thief/detail/<int:pk>', ThiefDetailView.as_view(), name='thief_profile'),
]
