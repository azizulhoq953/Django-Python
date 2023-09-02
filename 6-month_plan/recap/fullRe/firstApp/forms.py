from typing import Any, Dict
import email
from django import forms
from django.core import validators




class UserRegis(forms.Form):
    first_Name = forms.CharField()
    last_Name = forms.CharField()
    email = forms.EmailField(initial='example@gmail.com', required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)


    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repassword']
        if rightpass != wrongpass:
            raise forms.ValidationError('Password Doesnt match')