from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    birth_date = models.DateField('Fecha nacimiento', null=True, blank=True)
    phone = models.CharField('Telefono', max_length=15)
    is_librarian = models.BooleanField('Trabajador', default=False)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"