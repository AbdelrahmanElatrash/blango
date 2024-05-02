from django.db import models
from django.contrib.auth.models import AbstractUser , UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BlangoUserManager(UserManager):
    
    def _create_user(self,email,password,**extra_fields):
        if not email :
            raise ValuError ('email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None , **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_stuff') is not True :
            raise ValuError ('super user must have is_staff set to True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValuError ('super user mudt have is_superuser set to True')
        
        return self._create_user(email,password,**extra_fields)
        
        
        
        pass 
class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    
    objects =BlangoUserManager()
    
    USERNAME_FIELD ="email"
    REQUIRED_FIELDS =[]
    
    def __str__(self):
        return self.email
