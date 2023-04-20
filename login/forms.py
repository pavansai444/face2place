from django import forms
from .models import *

class passenger_form(forms.ModelForm):
    class Meta:
        model = passenger
        fields=["user_name","sex","status","balance","password","user"]