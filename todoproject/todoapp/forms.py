from .models import Task
from django import forms
 
class TodoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','style': 'width: 100%;'}),
            'priority':forms.NumberInput(attrs={'class':'form-control','style': 'width: 100%;'}),
            'date':forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control','style': 'width: 100%;'}),
        }

