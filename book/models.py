from django.db import models

class Book(models.Model):
    title = models.CharField('Título', max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(
        'author.Author',
        on_delete=models.CASCADE,
        related_name='books'
    )
    summary = models.TextField('Resumen', help_text='De qué trata el libro')
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    stock = models.PositiveIntegerField('Ejemplares disponibles', default=1)
    cover = models.ImageField('Portada', upload_to='covers/', null=True, blank=True)
    
    def __str__(self):
        return self.title