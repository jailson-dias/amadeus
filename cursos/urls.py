from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^cursos/(?P<slug>[\w_-]+)/$', views.Curso.as_view(),name='curso'),
    url(r'^categorias/(?P<slug>[\w_-]+)/$', views.CategoriaView.as_view(), name='categoria'),
    url(r'^perfil/(?P<slug>[\w_-]+)/$', views.AlunoView.as_view(), name='aluno'),
]
