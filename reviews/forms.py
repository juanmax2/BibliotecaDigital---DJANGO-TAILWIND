

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'mb-3 px-2 appearance-none border-t-0 border-l-0 border-r-0 border-b border-teal-500 focus:ring-0 focus:border-teal-700', 'id': 'rating'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'class': 'mb-3 px-2 appearance-none border-t-0 border-l-0 border-r-0 border-b border-teal-500 focus:ring-0 focus:border-teal-700', 'placeholder': 'Escribe tu comentario aquí...', 'id':'comment'}),
        }