# coding=utf-8

from django.shortcuts import render,get_object_or_404

from .models import Curso,Categoria,Aluno
from .formularios import Curso as C

def index(request):
    context = {
        'cursos': Curso.objects.filter(is_approved=True)
    }
    return render(request, 'cursos/base.html', context)

def curso(request, slug):
    context = {}
    instance = get_object_or_404(Curso, slug=slug)
    curso = C(instance=instance)

    if request.POST:
        curso = C(request.POST or None, instance=instance)
        if curso.is_valid():
            curso.save()
            context['sucesso'] = True

    context['curso'] = instance
    context['update'] = curso
    return render(request, 'cursos/curso.html', context)

def categoria_f(request, slug):
    context = {}
    categoria = get_object_or_404(Categoria, slug=slug)
    context['categoria'] = categoria
    context['cursos'] = categoria.cursos.filter(is_approved=True)
    return render(request, 'cursos/categoria.html', context)

def aluno(request, slug):
    context = {}
    aluno = get_object_or_404(Aluno, slug=slug)
    context['aluno'] = aluno
    context['cursos'] = aluno.curso_set.all()
    return render(request, 'cursos/aluno.html', context)
