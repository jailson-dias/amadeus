from .models import Categoria,Curso
from contas.models import User


def categorias(request):
    return {
        'categorias_cp': Categoria.objects.all()
    }

def alunos(request):
    return {
        'alunos_cp': User.objects.all()
    }

def cursos(request):
    return {
        'cursos_cp': Curso.objects.all()
    }
