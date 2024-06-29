# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, telefono, contrasena=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
        )
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, apellido, telefono, contrasena):
        user = self.create_user(
            email,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            contrasena=contrasena,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name='Correo Electrónico', max_length=255, unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
