from django import forms
from .models import TrashRequest, FundRequest

input_class = 'w-full rounded-lg border border-slate-300 bg-slate-50 p-3 text-sm text-slate-800 focus:border-blue-600 focus:outline-none focus:ring-1 focus:ring-blue-600 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200 dark:focus:border-blue-600 sm:text-base'
class TrashRequestForm(forms.ModelForm):
    class Meta:
        model = TrashRequest
        fields = ['trash_type', 'trash_types', 'pickup', 'DropOff', 'location', 'Phone']
        widgets = {
            'location': forms.TextInput(attrs={
            'placeholder': 'Your Address: 123ab Street city state',
            'class': input_class
            }),
            'Phone': forms.TextInput(attrs={
            'placeholder': 'Enter your Available Contact for pickup',
            'class': input_class
            }),
            
        }



class FundRequestForm(forms.ModelForm):
    class Meta:
        model = FundRequest
        fields = ['withdraw_type', 'amount', 'account_no', 'data_choice', 'airtime_choice', 'school_choice', 'health_choice', 'bank', "Phone", 'account_name', "others"]
        widgets = {
            'amount': forms.TextInput(attrs={
            'placeholder': 'Withdrawal Amount',
            'class': input_class
            }),
            'account_no': forms.TextInput(attrs={
            'placeholder': 'Your Account no.',
            'class': input_class
            }),
            'Phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number', 
                'class': input_class
            }),
            'account_name': forms.TextInput(attrs={
                'placeholder': 'Account Name', 
                'class': input_class
            }),
            'bank': forms.TextInput(attrs={
                'placeholder': 'Your bank', 
                'class': input_class
            }),
            'others': forms.TextInput(attrs={
                'placeholder': 'Your Reason for withdrawing', 
                'class': input_class
            })
        }

