from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^criar-conta/$', views.cadastro_aluno, name='cadastro_aluno'),
	url(r'^criar-professor/$', views.cadastro_professor, name='cadastro_professor'),
	url(r'^editar/$', views.editar, name='editar'),
]
