from django import forms
from .models import TrashRequest, FundRequest

input_class = 'w-full rounded-lg border border-slate-300 bg-slate-50 p-3 text-sm text-slate-800 focus:border-blue-600 focus:outline-none focus:ring-1 focus:ring-blue-600 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200 dark:focus:border-blue-600 sm:text-base'
class TrashRequestForm(forms.ModelForm):
    class Meta:
        model = TrashRequest
        fields = ['trash_type', 'trash_types', 'location', 'Phone', 'pickup', 'DropOff']
        widgets = {
            'location': forms.TextInput(attrs={
            'placeholder': 'Your Address: 123ab Street city state',
            'class': input_class
            }),
            'Phone': forms.TextInput(attrs={
            'placeholder': 'Enter the Phone No. to Contact regarding the Request.',
            'class': input_class
            }),
            
        }



class FundRequestForm(forms.ModelForm):
    class Meta:
        model = FundRequest
        fields = ['withdraw_type', 'amount', 'account_no']
        widgets = {
            'amount': forms.TextInput(attrs={
            'placeholder': 'Withdrawal Amount',
            'class': input_class
            }),
            'account_no': forms.TextInput(attrs={
            'placeholder': 'Your Account no.',
            'class': input_class
            }),
        }

