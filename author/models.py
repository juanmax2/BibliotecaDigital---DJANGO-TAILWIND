from django.db import models


class Author(models.Model):
    name = models.CharField('Nombre', max_length=150)
    last_name = models.CharField('Apellido', max_length=150)
    biography = models.TextField('Biografía', blank=True)
    image = models.ImageField('Imagen', upload_to='', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self):
        return f"{self.name} {self.last_name}"
    
    