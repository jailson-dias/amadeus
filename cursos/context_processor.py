from .models import Categoria,Aluno,Curso


def categorias(request):
    return {
        'categorias_cp': Categoria.objects.all()
    }

def alunos(request):
    return {
        'alunos_cp': Aluno.objects.all()
    }

def cursos(request):
    return {
        'cursos_cp': Curso.objects.all()
    }
