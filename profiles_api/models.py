from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin


class UserProfile (AbstractBaseUser, PermissionMixin):
    """modelo base de datos para usuarios en el sistema"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length = 255)
    is_activate = models.BooleanField (default = True)
    is_staff = models.BooleanField ( default = False)    
    
    objects = UserProfileManager() 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name (self): 
        """""Obtner nombre completo del usuario"""
        return self.name
    
        
    def get_short_name (self): 
        """obtener nombre corto del usuario"""
        return self.name
    
    def _str_(self):
        '''''Retornar cadena ''''