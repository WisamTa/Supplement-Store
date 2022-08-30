from django import forms
from .models import Review


class Add_ReviewForm(forms.ModelForm):
    """
    A class for the add review model form
    """
    class Meta:
        """
        A class for Meta information
        """
        model = Review

        fields = (
            'rating',
            'review_text',
        )
