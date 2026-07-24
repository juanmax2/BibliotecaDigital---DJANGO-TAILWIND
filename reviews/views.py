from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from book.models import Book
from reviews.forms import ReviewForm
# Create your views here.

@login_required
def add_review(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
    
    return redirect('book_detail',slug=slug)