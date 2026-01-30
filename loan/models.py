from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError

def get_maximo_retorno():
    return timezone.now() + timedelta(days=15)

class Loan(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='loans',
        verbose_name='Socio'
    )
    
    book = models.ForeignKey(
        'book.Book',
        on_delete=models.CASCADE,
        related_name='loans',
        verbose_name='Libro'
    )
    
    loan_date = models.DateTimeField('Fecha de préstamo', auto_now_add=True)
    
    maximo_retorno = models.DateTimeField('Fecha límite', default=get_maximo_retorno)
    
    return_date = models.DateTimeField('Fecha de devolución', null=True, blank=True)
    
    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('returned', 'Devuelto'),
        ('overdue', 'Atrasado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
        
    def __str__(self):
        return f"{self.book.title} - {self.user.username}"
    
    @property
    def is_overdue(self):
        if self.status == 'active' and timezone.now() > self.maximo_retorno:
            return True
        return False
    
    def save(self, *args, **kwargs):
        if not self.pk: # Creación
            if self.book.stock > 0:
                self.book.stock -= 1
                self.book.save()
            else:
                raise ValidationError("Sin stock")
            
        else:
            original_loan = Loan.objects.get(pk=self.pk)
            if original_loan.status != 'returned' and self.status == 'returned':
                self.book.stock += 1
                self.book.save()
                self.return_date = timezone.now()
            
        super().save(*args, **kwargs)