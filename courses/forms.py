from django import forms
from .models import Student

class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


    def __init__(self, *args, **kwargs):
        available_courses = kwargs.pop('available_courses', None)
        super().__init__(*args, **kwargs)

