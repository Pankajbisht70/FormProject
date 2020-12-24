from django import forms
from .models import *


class Indiajobsform(forms.ModelForm):
    class Meta:
        model = IndiaJobs
        fields ='__all__'




