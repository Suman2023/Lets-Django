from .models import Employee
from django import forms
from django.forms.fields import CharField

gender_choices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]
dept_choices = [
    ('FS', "Full Stack"),
    ('FE', 'Front End'),
    ('BE', 'Backend'),
]


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(choices=gender_choices, required=True)
    department = forms.ChoiceField(choices=dept_choices, required=True)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'department', 'gender')
