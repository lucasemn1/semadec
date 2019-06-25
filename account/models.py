from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import re
    
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, matricula, nome, email, password, cpf=None):
        user = self.model(matricula=matricula, nome=nome, email=email, cpf=cpf, password=password)
        user.set_password(password)
        # user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, nome, email, password, cpf):
        user=self.create_user(matricula=matricula, nome=nome, email=email, password=password, cpf=cpf)
        user.is_active = True
        # user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, matricula):
        return self.get(matricula=matricula)

class Usuario(AbstractBaseUser, PermissionsMixin):

    matricula = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(_('nome'), max_length=255)
    email = models.EmailField(_('email'), max_length=255, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    # date_joined = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['nome', 'email', 'cpf']
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
        
    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome
        
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    # def get(self, **extra_fields):
    #     return self.objects.get(**extra_fields)

    @property
    def is_staff(self):
        return self.nivelDeSeguranca == 2 if False else True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

# class Usuario(AbstractUser):
#     matricula = models.CharField(max_length=14, primary_key=True)
#     nome = models.CharField(_('nome'), max_length=255)
#     email = models.EmailField(_('email'), max_length=255, unique=True)
#     cpf = models.CharField(max_length=11, unique=True)
#     nivelDeSeguranca = models.IntegerField(default=2)
#     date_joined = models.DateTimeField(auto_now_add=True)