# coding=utf-8

from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage
from django.views import generic
from django.views.generic import base, edit,detail
from django.core.urlresolvers import reverse
from rolepermissions.verifications import has_role
from django.db.models.query import QuerySet

from .models import Categoria, Aluno_curso
from .models import Curso as C
from contas.models import User


class Index(generic.ListView):

    # queryset = C.objects.filter(is_approved=True)
    context_object_name = 'meus_cursos'
    paginate_by = 2
    template_name = 'cursos/base.html'

    def get_queryset(self):
        cursos = []
        if has_role(self.request.user,'aluno'):
            for curso in self.request.user.alunos_curso.all():
                if curso.curso.is_approved:
                    cursos.append(curso.curso)
        return cursos

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        if has_role(self.request.user,'aluno'):
            cursos = []
            meus_cursos = []
            for curso in self.request.user.alunos_curso.all():
                if curso.curso.is_approved:
                    meus_cursos.append(curso.curso)

            for curso in C.objects.filter(is_approved=True):
                if not curso in meus_cursos:
                    cursos.append(curso)

            paginator = Paginator(cursos, 2)
            try:
                page_number = int(self.request.GET.get('page', 1))
            except ValueError:
                raise Http404
            try:
                page_obj = paginator.page(page_number)
            except EmptyPage:
                raise Http404

            context['outros_cursos'] = page_obj.object_list
            context['paginacao'] = paginator
            context['pagina_obj'] = page_obj
        return context

# def index(request):
#     context = {
#         'cursos': Curso.objects.filter(is_approved=True)
#     }
#     return render(request, 'cursos/index.html', context)
class Curso(edit.UpdateView):
    model = C
    fields = ['is_approved']
    template_name = "cursos/curso.html"
    def get_success_url(self):
        return reverse('cursos:curso', kwargs={"slug":self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super(Curso, self).get_context_data(**kwargs)
        modulos = self.object.modulos.filter(is_visivel=True)
        alunos = []
        for aluno in self.object.cursos_aluno.all():
            alunos.append(aluno.aluno)
        context['alunos'] = alunos
        cursos = []
        if has_role(self.request.user,'aluno'):
            for curso in self.request.user.alunos_curso.all():
                cursos.append(curso.curso)
            if self.object in cursos:
                context['cadastrado'] = True
        # print (dir(self.object.mo))
        paginator = Paginator(modulos, 2)
        try:
            page_number = int(self.request.GET.get('page', 1))
        except ValueError:
            raise Http404
        try:
            page_obj = paginator.page(page_number)
        except EmptyPage:
            raise Http404

        context['paginator'] = paginator
        context['page_obj'] = page_obj
        context['modulos'] = page_obj.object_list
        return context

    def form_valid(self, form):
        if has_role(self.request.user,'professor'):
            context = super(Curso, self).form_valid(form)
            context['sucesso'] = True
        elif has_role(self.request.user,'aluno'):
            # print (type(self.request.user))
            aluno = Aluno_curso(aluno=self.request.user,curso=self.object)
            aluno.save()
            # print (aluno)
            context = HttpResponseRedirect(self.get_success_url())
            context['sucesso'] = True
        else:
            context = HttpResponseRedirect(self.get_success_url())
        return context
# def curso(request, slug):
#     context = {}
#     instance = get_object_or_404(Curso, slug=slug)
    # curso = C(instance=instance)

    # if request.POST:
    #     curso = C(request.POST or None, instance=instance)
    #     if curso.is_valid():
    #         curso.save()
    #         context['sucesso'] = True
    #
    # context['curso'] = instance
    # context['update'] = curso
    # return render(request, 'cursos/curso.html', context)

class CategoriaView(detail.DetailView):

    context_object_name = 'categoria'
    template_name = 'cursos/categoria.html'
    model = Categoria

    def get_context_data(self, **kwargs):
        context = super(CategoriaView, self).get_context_data(**kwargs)
        context['cursos'] = self.object.cursos.filter(is_approved=True)
        return context

# def categoria_f(request, slug):
#     context = {}
#     categoria = get_object_or_404(Categoria, slug=slug)
#     context['categoria'] = categoria
#     context['cursos'] = categoria.cursos.filter(is_approved=True)
#     return render(request, 'cursos/categoria.html', context)

class AlunoView(detail.DetailView):

    context_object_name = 'aluno'
    template_name = 'cursos/aluno.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(AlunoView, self).get_context_data(**kwargs)
        cursos = []
        for curso in self.object.alunos_curso.all():
            cursos.append(curso.curso)
        context['cursos'] = cursos
        return context

# def aluno(request, slug):
#     context = {}
#     aluno = get_object_or_404(Aluno, slug=slug)
#     context['aluno'] = aluno
#     context['cursos'] = aluno.curso_set.all()
#     return render(request, 'cursos/aluno.html', context)
