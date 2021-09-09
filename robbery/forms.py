from django import forms

from .models import Robbery


class RobberyForm(forms.ModelForm):

    class Meta:
        model = Robbery
        fields = '__all__'
