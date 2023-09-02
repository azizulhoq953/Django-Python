import email
from django import forms 
from django.core import validators

class StudentsReg(forms.Form):
    first_name = forms.CharField(initial="Your name",)
    last_name = forms.CharField()
    email = forms.EmailField(initial='example@gmail.com', disabled=False)
    # fullName = forms.TextInput(attrs={"required": True})
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)
    # email.clean("foo@example.com")

    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repassword']
        if rightpass != wrongpass:
            raise forms.ValidationError("Password Dosen't match")