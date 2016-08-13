from django.shortcuts import render
from .formularios import Categoria, Curso,Modulo,Add_aluno_curso, Material, Atividade
from django.db import IntegrityError
from rolepermissions.decorators import has_role_decorator,has_permission_decorator
# from rolepermissions.verifications import has_permission

def categoria_f(request):
    context = {}
    categoria = Categoria(request.POST or None)

    if categoria.is_valid():
        categoria.save()
        context['sucesso'] = True
        categoria = Categoria()
    context['categoria'] = categoria
    return render(request,"formularios/categoria.html",context)

@has_permission_decorator('criar_cursos')
def curso_f(request):
    context = {}
    curso = Curso(request.POST or None,request.FILES or None)
    if curso.is_valid():
        curso.save()
        context['sucesso'] = True
        curso = Curso()
    context['curso'] = curso
    return render(request,"formularios/curso.html",context)

# def aluno_f(request):
#     context = {}
#     aluno = Aluno(request.POST or None, request.FILES or None)
#     if aluno.is_valid():
#         aluno.save()
#         context['sucesso'] = True
#         aluno = Aluno()
#     context['aluno'] = aluno
#     return render(request,"formularios/aluno.html",context)

@has_role_decorator('professor')
def modulo_f(request):
    context = {}
    modulo = Modulo(request.POST or None)
    if modulo.is_valid():
        modulo.save()
        context['sucesso'] = True
        modulo = Modulo()
    context['modulo'] = modulo
    return render(request,"formularios/modulo.html",context)

# def aluno_curso(request):
#     context = {}
#     aluno = Add_aluno_curso(request.POST or None)
#     if aluno.is_valid():
#         aluno.save()
#         context['sucesso'] = True
#         aluno = Add_aluno_curso()
#     context['aluno'] = aluno
#     return render(request,"formularios/aluno_curso.html",context)

def material_f(request):
    context = {}
    material = Material(request.POST or None)
    if material.is_valid():
        material.save()
        context['sucesso'] = True
        material = Material()
    context['aluno'] = material
    return render(request,"formularios/aluno_curso.html",context)

def atividade_f(request):
    context = {}
    atividade = Atividade(request.POST or None)
    if atividade.is_valid():
        atividade.save()
        context['sucesso'] = True
        atividade = Atividade()
    context['aluno'] = atividade
    return render(request,"formularios/aluno_curso.html",context)
