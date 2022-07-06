from django import forms
from django.contrib.auth import get_user_model

from tally.users.models import CustomerRelation

User = get_user_model()


class NewValuerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'national_id']


class CustomerRelationForm(forms.ModelForm):
    class Meta:
        model = CustomerRelation
        fields = '__all__'
