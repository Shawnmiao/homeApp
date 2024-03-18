from django import forms
from .models import Staff

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