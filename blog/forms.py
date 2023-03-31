from django.forms import ModelForm
from.models import Blog
from django import forms

class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields = '__all__'

        widgets={
            'created_at':forms.DateInput(attrs={'type':'date'}),
        }