from django import forms
from .models import TrashRequest

class TrashRequestForm(forms.ModelForm):
    class Meta:
        model = TrashRequest
        fields = ['trash_type', 'trash_types']
