from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = Feedback
        fields = ("name", "email", "text")
