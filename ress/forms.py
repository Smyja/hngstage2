from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from . import models
from .models import Contact

class ContactForm(forms.ModelForm):
   
    email = forms.CharField(help_text="Your email")
    description = forms.CharField(help_text="Your message")
    class Meta:
        model = Contact
        fields = [
            "email", 
            "description"
            
        ]