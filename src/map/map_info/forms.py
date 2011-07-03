from django import forms
from map.map_info.models import Layer, Comment

class AddPointForm(forms.Form):
    
    """New points form.

    The user has to enter the following details for new points:
      later: chosen from a drop down list.
      report_date: entered manually. but must adhere to the django date format
      subject: point subject. displayed as a text box.
      description: point description. displayed as a text box.
      file: chosen from a file browser window.
      point: represented as latitude and longitude. chosen using map widget

    """

    layer = forms.ModelChoiceField(Layer.objects.all())
    report_date = forms.DateField()
    subject = forms.CharField()
    description = forms.CharField()
    file = forms.FileField()
    point = forms.CharField()

class CommentForm(forms.ModelForm):

    """ New comments form

    we only need the comment body, comment author are extracted from the
    currently logged in user.  date is set to the current date.
    
    """

    class Meta:
        model = Comment
        exclude = ["post", "author"]