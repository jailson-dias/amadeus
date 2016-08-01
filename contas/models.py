import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=100, blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
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
    estado = models.CharField('Estado', choices=ESTADOS,max_length=100)
    telefone = models.CharField('Telefone', max_length=100, blank=True)
    is_staff = models.BooleanField('Admin', default=False)
    is_professor = models.BooleanField('Professor', default=False)
    data_entrou = models.DateTimeField('Data de Entrada', auto_now_add=True)
    data_atualizou = models.DateTimeField('Data de Última Atualização', auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self.name.split(" "))
