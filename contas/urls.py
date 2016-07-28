from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^criar-conta/$', views.usuario, name='usuario'),
]