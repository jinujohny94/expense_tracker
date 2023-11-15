from django import forms
from firstapp.models import Employee

class UserForm(forms.Form):
    user_name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'