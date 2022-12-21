from django import forms 
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'moyenne']
    labels = {
      'student_number': 'Student Number', 
      'first_name': 'First Name', 
      'last_name': 'Last Name', 
      'email': 'Email', 
      'field_of_study': 'Field of Study', 
      'moyenne': 'moyenne'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'moyenne': forms.NumberInput(attrs={'class': 'form-control'}),
    }