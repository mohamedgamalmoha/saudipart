from django.urls import path
from .views import HomeView, RobberyView, RobberyListView, RobberyListViewAdmin, robbery_profile, export_csv

app_name = 'robbery'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('robbery/add', RobberyView.as_view(), name='robbery_add'),
    path('robbery/list', RobberyListView.as_view(), name='robbery_list'),
    path('robbery/list/admin', RobberyListViewAdmin.as_view(), name='robbery_list_admin'),
    path('robbery/profile/<str:iban>', robbery_profile, name='robbery_profile'),
    path('robbery/profile/<str:iban>/csv_export', export_csv, name='robbery_profile_export_csv'),
]
