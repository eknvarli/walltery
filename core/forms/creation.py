from django import forms
from core.models import Password


class Creation(forms.ModelForm):
    class Meta:
        model = Password
        fields = ('title', 'password', 'description')