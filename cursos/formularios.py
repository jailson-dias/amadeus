from django import forms
from .models import Curso

class Curso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['is_approved']
