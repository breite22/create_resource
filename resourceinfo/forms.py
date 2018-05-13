from django import forms
from django.core.exceptions import ValidationError


from .models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['resource_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['resource_content'].strip()
