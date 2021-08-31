from django import forms

from .models import Thief, Victim


class VictimForm(forms.ModelForm):

    class Meta:
        model = Victim
        fields = '__all__'
        labels = {
            'thief': 'Thief Ip Number',
        }
        help_texts = {
            'thief': 'In case you didn\'t`t find it go to thief form and add it, link is down bellow',
        }
        error_messages = {
            'thief': {
                'unique': "This Ip ia already exists, go to victim form, link is down bellow",
            },
        }


class ThiefForm(forms.ModelForm):

    class Meta:
        model = Thief
        fields = '__all__'
