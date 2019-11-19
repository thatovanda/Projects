from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'telephone', 'email', 'fax', 'vat_number')
