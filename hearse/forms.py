from django import forms
from .models import Hearse, Request

class user_detail(forms.ModelForm):

    class Meta:
        model = Request
        fields = '__all__'

