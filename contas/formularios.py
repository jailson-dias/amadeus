from django.contrib.auth.forms import UserCreationForm
from .models import User

class Usuario(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','name','email','cpf','cidade','estado','telefone']
