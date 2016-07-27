from django import forms
from cursos.models import Curso as C, Aluno as A, Categoria as Cat, Modulo as M, Aluno_curso, Material as Mat, Atividade as At

class Categoria(forms.ModelForm):
    nome = forms.CharField(label='Categoria')

    class Meta:
        model = Cat
        fields = ['nome']

class Curso(forms.ModelForm):

    # curso = forms.CharField(label='Curso')
    # professor = forms.CharField(label='Professor')
    # data_inicio = forms.DateField(label='Inicio')
    # data_fim = forms.DateField(label='Fim')
    # # slug = models.SlugField('Identificador',max_length=100,unique=True)
    # descricao = forms.CharField(label='Descrição', widget=forms.Textarea(), initial='Descrição')
    # sobre = forms.CharField(label='Sobre', widget=forms.Textarea(), initial='Sobre')
    # is_approved = forms.BooleanField(label='Visivel',initial=False)
    # # alunos = forms.ModelMultipleChoiceField(label='Alunos',queryset=A.objects.all())
    # categoria = forms.ModelChoiceField(label='Categoria',widget=forms.Select(),queryset=Cat.objects.all())
    # imagem = forms.ImageField(label='Imagem')

    class Meta:
        model = C
        fields = ['curso','professor','data_inicio','data_fim','descricao','sobre','is_approved','categoria','imagem']
        # fields = '__all__'

class Aluno(forms.ModelForm):

    class Meta:
        model = A
        fields = '__all__'

class Modulo(forms.ModelForm):

    class Meta:
        model = M
        fields = '__all__'

class Add_aluno_curso(forms.ModelForm):

    class Meta:
        model = Aluno_curso
        fields = '__all__'

class Material(forms.ModelForm):

    class Meta:
        model = Mat
        fields = '__all__'

class Atividade(forms.ModelForm):

    class Meta:
        model = At
        fields = '__all__'
