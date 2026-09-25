from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']
        labels = {'title':''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields  = ['content']
        labels = {'content':''}
        widgets = {'content': forms.Textarea(attrs={'cols':80})}