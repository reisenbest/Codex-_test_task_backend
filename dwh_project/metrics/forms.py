<<<<<<< HEAD
from django import forms
from .models import Metric

class MetricForm(forms.ModelForm):
    class Meta:
        model = Metric

        fields = '__all__'