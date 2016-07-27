# coding=utf-8

from django.db import models
from autoslug.fields import AutoSlugField

class Aluno(models.Model):
	nome = models.CharField('nome',max_length=100)
	email = models.EmailField('Email',max_length=100)
	slug = AutoSlugField(populate_from='nome',unique=True)
	telefone = models.CharField('Telefone',max_length=50)
	imagem = models.ImageField(upload_to='alunos/imagens',verbose_name='Imagem', null=True,blank=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Aluno'
		verbose_name_plural = 'Alunos'

class Categoria(models.Model):
	nome = models.CharField(verbose_name='nome',max_length=100, unique=True)
	# slug = AutoSlugField(models.SlugField('Slug',max_length=100,unique=True))
	slug = AutoSlugField(populate_from='nome',unique=True)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return self.nome

class Curso(models.Model):
	curso = models.CharField('nome',max_length=100)
	professor = models.CharField('Professor',max_length=100)
	data_inicio = models.DateField('Inicio')
	data_fim = models.DateField('Fim')
	slug = AutoSlugField(populate_from='curso',unique=True)
	descricao = models.TextField('Descrição', blank=True)
	sobre = models.TextField('Sobre', blank=True)
	is_approved = models.BooleanField('Aprovado', default=False, blank=True)
	alunos = models.ManyToManyField(Aluno, verbose_name='alunos',through='Aluno_curso', blank=True)
	categoria = models.ForeignKey(Categoria, verbose_name='categoria', related_name="cursos")
	imagem = models.ImageField(upload_to='imagens/',verbose_name='Imagem',null=True,blank=True)

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'

	def __str__(self):
		return self.curso

class Aluno_curso(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Modulo(models.Model):
	nome = models.CharField('nome',max_length=100)
	slug = AutoSlugField(populate_from='nome',unique=True)
	descricao = models.TextField('Descrição',blank=True)
	is_visivel = models.BooleanField('Visivel',default=False, blank=True)
	curso = models.ForeignKey(Curso, verbose_name='curso', related_name='modulos')

	class Meta(object):
		verbose_name = "Modulo"
		verbose_name_plural = "Modulos"

	def __str__(self):
		return self.nome

class Material(models.Model):
	nome = models.CharField('nome',max_length=100)
	slug = AutoSlugField(populate_from='nome',unique=True)
	modulo_atual = models.ForeignKey(Modulo, verbose_name='modulo',related_name='materiais')
	tipo = models.CharField('tipo',max_length=100)

	class Meta(object):
		verbose_name = "Material"
		verbose_name_plural = "Materiais"

	def __str__(self):
		return self.nome

class Atividade(models.Model):
	nome = models.CharField('nome',max_length=100)
	slug = AutoSlugField(populate_from='nome',unique=True)
	modulo_atual = models.ForeignKey(Modulo, verbose_name='modulo',related_name='atividades')
	tipo = models.CharField('tipo',max_length=100)

	class Meta(object):
		verbose_name = "Atividade"
		verbose_name_plural = "Atividades"

	def __str__(self):
		return self.nome
