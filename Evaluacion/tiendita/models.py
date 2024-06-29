from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.email