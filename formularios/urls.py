from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cursos/$', views.curso_f, name='curso'),
    url(r'^categorias/$', views.categoria_f, name='categoria'),
    # url(r'^alunos/$', views.aluno_f, name='aluno'),
    url(r'^modulo/$', views.modulo_f, name='modulo'),
    # url(r'^add-aluno-curso/$', views.aluno_curso, name='add_aluno'),
    url(r'^add-material/$', views.material_f, name='add_material'),
    url(r'^add-atividade/$', views.atividade_f, name='add_atividade'),
]
