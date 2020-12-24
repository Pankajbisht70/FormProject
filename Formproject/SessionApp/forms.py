from django import forms
from .models import *


class Personal_form(forms.ModelForm):
    class Meta:
        model = Personal_info
        fields ='__all__'


class Academic_form(forms.ModelForm):
    class Meta:
        model = Academic_info
        fields ='__all__'


class Experience_form(forms.ModelForm):
    class Meta:
        model = Experience_info
        fields ='__all__'
