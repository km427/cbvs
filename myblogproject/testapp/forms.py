from django import forms
class sharebyemail(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

from testapp.models import comments
class commentsform(forms.ModelForm):
    class Meta:
        model=comments
        fields=('name','email','body')