from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE

# Create your models here.

gender_choices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


class Person(models.Model):
    gender_choices = gender_choices
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=1,
                              choices=gender_choices,
                              help_text="Select your gender")

    def __str__(self):
        return self.first_name


class Employee(models.Model):
    dept_choices = [
        ('FS', "Full Stack"),
        ('FE', 'Front End'),
        ('BE', 'Backend'),
    ]
    profile = models.ForeignKey('Person', on_delete=models.CASCADE)
    department = models.CharField(max_length=2,
                                  choices=dept_choices,
                                  default="department")

    def __str__(self):
        return self.profile.first_name + '(' + self.department + ')'
