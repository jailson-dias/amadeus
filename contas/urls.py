from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^criar-conta/$', views.CadatroAlunoView.as_view(), name='cadastro_aluno'),
	url(r'^criar-professor/$', views.CadatroProfessorView.as_view(), name='cadastro_professor'),
	url(r'^editar/$', views.editar, name='editar'),
]
