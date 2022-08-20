from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A class for the contact form
    """
    class Meta:
        """
        A class for Meta information
        """
        model = Contact
        fields = '__all__'