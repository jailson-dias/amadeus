from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cursos/([\w_-]+)/$', views.curso, name='curso'),
    url(r'^categorias/([\w_-]+)/$', views.categoria_f, name='categoria'),
    url(r'^perfil/([\w_-]+)/$', views.aluno, name='aluno'),
]
