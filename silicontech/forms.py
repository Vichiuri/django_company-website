from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()()
        fields = ['name', 'national_id']
