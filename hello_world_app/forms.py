from django import forms
from .models import GradeEntry

class GradeEntryForm(forms.ModelForm):
    class Meta:
        model = GradeEntry
        fields = ['course_name', 'current_grade', 'desired_grade', 'final_weight']
        labels = {
            'course_name': 'Course Name',
            'current_grade': 'Current Grade (%)',
            'desired_grade': 'Desired Grade (%)',
            'final_weight': 'Final Exam Weight (%)',
        }
        widgets = {
            'course_name': forms.TextInput(attrs={'placeholder': 'e.g. Math 101'}),
            'current_grade': forms.NumberInput(attrs={'placeholder': 'e.g. 78', 'step': '0.01', 'min': '0', 'max': '100'}),
            'desired_grade': forms.NumberInput(attrs={'placeholder': 'e.g. 85', 'step': '0.01', 'min': '0', 'max': '100'}),
            'final_weight': forms.NumberInput(attrs={'placeholder': 'e.g. 30', 'step': '0.01', 'min': '0', 'max': '100'}),
        }

