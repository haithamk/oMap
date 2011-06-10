from django import forms

class AddPointForm(forms.Form):
    report_date = forms.DateField()
    subject = forms.CharField()
    description = forms.CharField()
    file = forms.CharField()
