# coding=utf-8

from django.db import models
from autoslug.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _

from contas.models import User

# class Aluno(models.Model):
# 	nome = models.CharField(_('Name'),max_length=100)
# 	email = models.EmailField(_('E-mail'),max_length=100)
# 	slug = AutoSlugField(populate_from='nome',unique=True)
# 	telefone = models.CharField(_('Telephone'),max_length=50)
# 	imagem = models.ImageField(upload_to='alunos/imagens',verbose_name=_('Image'), null=True,blank=True)
#
# 	def __str__(self):
# 		return self.nome
#
# 	class Meta:
# 		verbose_name = _('Student')
# 		verbose_name_plural = _('Students')

class Categoria(models.Model):
	nome = models.CharField(verbose_name=_('Name'),max_length=100, unique=True)
	slug = AutoSlugField(populate_from='nome',unique=True)

	class Meta:
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')

	def __str__(self):
		return self.nome

class Curso(models.Model):
	curso = models.CharField(_('Name'),max_length=100)
	# professor = models.CharField(_('Professor'),max_length=100)
	data_inicio = models.DateField(_('Begin'))
	data_fim = models.DateField(_('End'))
	slug = AutoSlugField(populate_from='curso',unique=True)
	descricao = models.TextField(_('Description'), blank=True)
	sobre = models.TextField(_('About'), blank=True)
	is_approved = models.BooleanField(_('Approved'), default=False, blank=True)
	# alunos = models.ManyToManyField(Aluno, verbose_name=_('Students'),through='Aluno_curso', blank=True)
	categoria = models.ForeignKey(Categoria, verbose_name=_('Category'), related_name="cursos")
	imagem = models.ImageField(upload_to='imagens/',verbose_name=_('Image'),null=True,blank=True)

	class Meta:
		verbose_name = _('Course')
		verbose_name_plural = _('Courses')

	def __str__(self):
		return self.curso

class Aluno_curso(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alunos_curso")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="cursos_aluno")
	# data_entrou = models.DateTimeField(_('Entry date'), auto_now_add=True)

class Professor_curso(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE,related_name="professor_curso")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE,related_name="cursos_professor")
	# data_entrou = models.DateTimeField(_('Entry date'), auto_now_add=True)

class Modulo(models.Model):
	nome = models.CharField(_('Name'),max_length=100)
	slug = AutoSlugField(populate_from='nome',unique=True)
	descricao = models.TextField(_('Description'),blank=True)
	is_visivel = models.BooleanField(_('Visible'),default=False, blank=True)
	curso = models.ForeignKey(Curso, verbose_name=_('Course'), related_name='modulos')

	class Meta(object):
		verbose_name = _("Module")
		verbose_name_plural = _("Modules")

	def __str__(self):
		return self.nome

class Material(models.Model):
	nome = models.CharField(_('Name'),max_length=100)
	slug = AutoSlugField(populate_from='nome',unique=True)
	modulo_atual = models.ForeignKey(Modulo, verbose_name=_('Module'),related_name='materiais')
	tipo = models.CharField(_('Type'),max_length=100)

	class Meta(object):
		verbose_name = _("Material")
		verbose_name_plural = _("Materials")

	def __str__(self):
		return self.nome

class Atividade(models.Model):
	nome = models.CharField(_('Name'),max_length=100)
	slug = AutoSlugField(populate_from='nome',unique=True)
	modulo_atual = models.ForeignKey(Modulo, verbose_name=_('Module'),related_name='atividades')
	tipo = models.CharField(_('Type'),max_length=100)

	class Meta(object):
		verbose_name = _("Activity")
		verbose_name_plural = _("Activities")

	def __str__(self):
		return self.nome
