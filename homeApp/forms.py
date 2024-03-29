from django import forms
from .models import Staff, Branch,Client

class StaffHireForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staffno', 'fname', 'lname', 'position', 'branchno', 'dob', 'salary', 'telephone', 'mobile', 'email']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'salary': forms.NumberInput(attrs={'step': '0.01'}),

        }
        labels={
            'staffno':'Staff No',
            'fname':'First Name',
            'lname':'Last Name',
            'position':'Position',
            'branchno':'branch No',
            'DOB':'dob',

        }

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch_no', 'street', 'city', 'postcode']  # List the fields you want to include in your form
        widgets = {
            'branch_no': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_no', 'first_name', 'last_name', 'tel_no', 'street', 'city', 'email', 'pref_type', 'max_rent']

class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'tel_no', 'street', 'city', 'email', 'pref_type', 'max_rent']