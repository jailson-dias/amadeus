from django.shortcuts import render
from rolepermissions.shortcuts import assign_role
from django.contrib.auth.decorators import login_required
from .formularios import Usuario
from .models import User

# @login_required
def cadastro_aluno(request):
    context = {}
    user = Usuario(request.POST or None,request.FILES or None)
    if user.is_valid():
        user.save()
        user = User.objects.get(username=user.cleaned_data['username'])
        assign_role(user, 'aluno')
        context['sucesso'] = True
        user = Usuario()
    context['usuario'] = user
    return render(request,"contas/usuario.html",context)

def cadastro_professor(request):
    context = {}
    user = Usuario(request.POST or None,request.FILES or None)
    if user.is_valid():
        user.save()
        user = User.objects.get(username=user.cleaned_data['username'])
        assign_role(user, 'professor')
        context['sucesso'] = True
        user = Usuario()
    context['usuario'] = user
    return render(request,"contas/usuario.html",context)

@login_required
def editar(request):
    context = {}
    instance = request.user
    user = Usuario(request.POST or None,request.FILES or None,instance=instance)
    if user.is_valid():
        user.save()
        context['sucesso'] = True
    context['usuario'] = user
    return render(request,"contas/editar.html",context)


def csrf_failure(request, reason=""):
    context = {}
    return render(request,"contas/403.html",context)
