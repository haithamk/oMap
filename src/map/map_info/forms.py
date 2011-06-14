from django import forms
from map_info.models import Layer, Comment

class AddPointForm(forms.Form):
    layer = forms.ModelChoiceField(Layer.objects.all())
    report_date = forms.DateField()
    subject = forms.CharField()
    description = forms.CharField()
    file = forms.FileField()
    point = forms.CharField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "author"]