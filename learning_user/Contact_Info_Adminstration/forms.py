from django import forms
from django.contrib.auth.models import User



def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    Sujet = forms.CharField(max_length=80)
    Message_Detailles = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])

