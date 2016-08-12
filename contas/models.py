import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        _('User'), max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                _('Enter a user name. This value should contain only letters, numbers and the characters: @/./+/-/_ .')
                ,'invalid'
            )
        ], help_text=_('A short name that will be used to identify you a unique way on the platform')
    )
    name = models.CharField(_('Name'), max_length=100, blank=True)
    email = models.EmailField(_('E-mail'), unique=True)
    cpf = models.CharField(_('CPF'), max_length=100, blank=True)
    cidade = models.CharField(_('City'), max_length=100, blank=True)
    ESTADOS = (
		("1","Acre"),
		("2","Alagoas"),
		("3","Amazonas"),
		("4","Amapá"),
		("5","Bahia"),
		("6","Ceará"),
		("7","Distrito Federal"),
		("8","Espírito Santo"),
		("9","Goiás"),
		("10","Maranhão"),
		("11","Mato Grosso"),
		("12","Mato Grosso do Sul"),
		("13","Minas Gerais"),
		("14","Pará"),
		("15","Paraíba"),
		("16","Paraná"),
		("17","Pernambuco"),
		("18","Piauí"),
		("19","Rio de Janeiro"),
		("20","Rio Grande do Norte"),
		("21","Rondônia"),
		("22","Rio Grande do Sul"),
		("23","Roraima"),
		("24","Santa Catarina"),
		("25","Sergipe"),
		("26","São Paulo"),
		("27","Tocantins")
    	)
    estado = models.CharField(_('State'), choices=ESTADOS,max_length=100)
    telefone = models.CharField(_('Telephone'), max_length=100, blank=True)
    is_staff = models.BooleanField(_('Admin'), default=False)
    is_professor = models.BooleanField(_('Professor'), default=False)
    data_entrou = models.DateTimeField(_('Entry date'), auto_now_add=True)
    data_atualizou = models.DateTimeField(_('Date of last update'), auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self.name.split(" "))
