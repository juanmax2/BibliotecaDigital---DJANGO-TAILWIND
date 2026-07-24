from django.db import models

from book.models import Book
from django.conf import settings

# Create your models here.

class Review(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        verbose_name="user"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="book"
    )
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1,6)], 
        verbose_name="valoración"
    )
    comment = models.TextField(verbose_name="comment")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    
    class Meta: 
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Reseña para {self.book.title}"
        