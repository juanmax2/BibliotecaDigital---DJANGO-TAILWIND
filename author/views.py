from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Author
from book.models import Book

class AuthorListView(ListView):
    model = Author
    template_name = 'core/author_list.html'
    context_object_name = 'authors'
    paginate_by = 9
    ordering = ['name']
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'core/author_detail.html'
    context_object_name = 'author'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['author_books'] = Book.objects.filter(author=self.object)
        return context