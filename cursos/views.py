# coding=utf-8

from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage
from django.views import generic
from django.views.generic import base, edit,detail
from django.core.urlresolvers import reverse

from .models import Categoria,Aluno
from .models import Curso as C

class Index(generic.ListView):

    queryset = C.objects.filter(is_approved=True)
    context_object_name = 'cursos'
    paginate_by = 2
    template_name = 'cursos/index.html'

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
        context = super(Curso, self).form_valid(form)
        context['sucesso'] = True
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
    model = Aluno

    def get_context_data(self, **kwargs):
        context = super(AlunoView, self).get_context_data(**kwargs)
        context['cursos'] = self.object.curso_set.all()
        return context

# def aluno(request, slug):
#     context = {}
#     aluno = get_object_or_404(Aluno, slug=slug)
#     context['aluno'] = aluno
#     context['cursos'] = aluno.curso_set.all()
#     return render(request, 'cursos/aluno.html', context)
