from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from book.models import Book
from .models import Loan
from django.contrib import messages
from django.views.generic import ListView

@login_required
def loan_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    
    active_loans_count = Loan.objects.filter(user=request.user, status='active').count()
    
    if active_loans_count >= 3:
        messages.add_message(request, messages.ERROR, "Has alcanzado el máximo de libros en préstamo.")
        return redirect('book_detail', slug=slug)
    
    if book.stock > 0:
        Loan.objects.create(user=request.user, book=book)
        messages.add_message(request, messages.SUCCESS, f"Has cogido prestado, {book.title}.")
    else:
        messages.add_message(request, messages.ERROR, f"Lo sentimos, no hay ejemplares disponibles.")
        
    return redirect('book_detail', slug=slug)


@login_required
def return_book(request, pk):
    loan = get_object_or_404(Loan, pk=pk, user=request.user, return_date__isnull=True)
    
    if loan.status != 'returned':
        loan.status = 'returned'
        
        loan.save()
        messages.add_message(request, messages.SUCCESS, f"Libro {loan.book.title} correctamente")
    else:
        messages.add_message(request, messages.INFO, "El libro ya estaba devuelto.")
        
    return redirect('my_loans')


        
class MyLoansView(LoginRequiredMixin, ListView):
    model = Loan
    template_name = 'core/my_loans.html'
    context_object_name = 'loans'
    
    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user).order_by('status', '-loan_date')
    