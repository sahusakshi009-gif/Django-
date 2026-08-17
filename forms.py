from django import forms
from .models import Employee, Department


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            'name',
            'email',
            'phone',
            'department',
            'salary',
            'joining_date'
        ]

        widgets = {
            'joining_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = [
            'name',
            'description'
        ]