from django.shortcuts import render

from django.views.generic import ListView
from book.models import Book

class HomeView(ListView):
    model = Book
    template_name = 'core/home.html'
    context_object_name = 'list_books'
    
    def get_queryset(self):
        return Book.objects.select_related('author').order_by('-id')[:10]


