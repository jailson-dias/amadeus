from django.shortcuts import render
from rolepermissions.shortcuts import assign_role
from django.contrib.auth.decorators import login_required
from django.views.generic import base, edit
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .formularios import Usuario
from .models import User

# @login_required
class CadatroAlunoView(edit.CreateView):
    model = User
    form_class = Usuario
    template_name = "contas/usuario.html"
    context_object_name = 'usuario'

    def get_success_url(self):
        return reverse('login')

    def get_context_data(self, **kwargs):
        context = super(CadatroAlunoView, self).get_context_data(**kwargs)
        # print ((context.keys()))

        return context

    def form_valid(self, form):
        context = super(CadatroAlunoView, self).form_valid(form)
        user = User.objects.get(username=form.cleaned_data['username'])
        assign_role(user, 'aluno')
        context['sucesso'] = True

        # print ((self.request.POST))
        # print ((form))
        # print (dir(form))
        return context


# def cadastro_aluno(request):
#     context = {}
#     user = Usuario(request.POST or None,request.FILES or None)
#     if user.is_valid():
#         user.save()
#         user = User.objects.get(username=user.cleaned_data['username'])
#         assign_role(user, 'aluno')
#         context['sucesso'] = True
#         user = Usuario()
#     context['usuario'] = user
#     return render(request,"contas/usuario.html",context)

class CadatroProfessorView(edit.CreateView):
    model = User
    form_class = Usuario
    template_name = "contas/usuario.html"
    context_object_name = 'usuario'

    def get_success_url(self):
        return reverse('login')

    def get_context_data(self, **kwargs):
        context = super(CadatroProfessorView, self).get_context_data(**kwargs)
        # print ((context.keys()))

        return context

    def form_valid(self, form):
        context = super(CadatroProfessorView, self).form_valid(form)
        user = User.objects.get(username=form.cleaned_data['username'])
        assign_role(user, 'professor')
        user.is_professor = True
        user.save()
        context['sucesso'] = True

        # print ((self.request.POST))
        # print ((form))
        # print (dir(form))
        return context

# def cadastro_professor(request):
#     context = {}
#     user = Usuario(request.POST or None,request.FILES or None)
#     if user.is_valid():
#         user.save()
#         user = User.objects.get(username=user.cleaned_data['username'])
#         assign_role(user, 'professor')
#         context['sucesso'] = True
#         user = Usuario()
#     context['usuario'] = user
#     return render(request,"contas/usuario.html",context)

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
