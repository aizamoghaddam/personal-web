from django import forms
from .models import *


class CommentForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'style': 'padding:0px 3px; font-size:15px; width:300px; height:30px;'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'style':'padding:0px 3px; font-size:15px; width:300px; height:30px;'
    }))
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'style':'width:400px; height:370px; padding:10px; font-size:15px;'
    }))