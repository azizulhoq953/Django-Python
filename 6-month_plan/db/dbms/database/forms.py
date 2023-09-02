from django import forms



class TeachersRegistration(forms.Form):
    firs_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()