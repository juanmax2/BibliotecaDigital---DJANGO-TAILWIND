from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'loan_date', 'status')
    list_filter = ('status', 'loan_date')
    search_fields = ('user__username', 'book__title')
