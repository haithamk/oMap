from django import forms
from map_info.models import Layer

class AddPointForm(forms.Form):
    layer = forms.ModelChoiceField(Layer.objects.all())
    report_date = forms.DateField()
    subject = forms.CharField()
    description = forms.CharField()
    file = forms.CharField()
    point = forms.CharField()
