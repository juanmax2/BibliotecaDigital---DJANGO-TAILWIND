from django.shortcuts import render

from reviews.forms import ReviewForm
from .models import Book
from django.views.generic import DetailView, ListView
from django.db.models import Q

# Create your views here.
class BookDetailView(DetailView):
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['form'] = ReviewForm()
        return context
    

class BookListView(ListView):
    model = Book
    template_name = 'core/book_list.html'
    context_object_name = 'books'
    paginate_by = 9
    ordering = ['title']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(author__name__icontains=query) |
                Q(author__last_name__icontains=query)
            )
            
        return queryset