from django import forms

from .models import Robbery


class RobberyForm(forms.ModelForm):

    class Meta:
        model = Robbery
        fields = '__all__'
        exclude = ['user', ]
        help_texts = {
            'outboard_transferred': 'هل تم التحويل النقود مباشرة الي اي بان العصابة ام انه تم عبر وسيط داخلي ',
        }
