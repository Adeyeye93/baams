from django import forms
from .models import TrashRequest, FundRequest

class TrashRequestForm(forms.ModelForm):
    class Meta:
        model = TrashRequest
        fields = ['trash_type', 'trash_types']

class FundRequestForm(forms.ModelForm):
    class Meta:
        model = FundRequest
        fields = ['withdraw_type', 'amount']
