# import os
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail

class AlunoTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('criar:aluno')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/aluno.html')
        # imagem_i = open('/home/jailson/Imagens/citi.png')
        #
        # print ("\n\n",imagem_i, "\n\njailson\n\n")
        data = {'nome': 'fulano', 'email': 'fulano@fulano.com', 'telefone':'(81) 987456321','imagem':''}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' in response.context)

    def test_not_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        # imagem_i = open('/home/jailson/Imagens/citi.png')
        #
        # print ("\n\n",imagem_i, "\n\njailson\n\n")
        data = {'nome': 'fulano', 'email': '','telefone':'(81) 987456321','imagem':''}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' not in response.context)
        self.assertFormError(response, 'aluno', 'email', 'Este campo é obrigatório.')

class CursoTestCase(TestCase):
    url_aluno = reverse('criar:aluno')
    url_categoria = reverse('criar:categoria')
    def setUp(self):
        self.client = Client()
        self.url = reverse('criar:curso')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/curso.html')
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' in response.context)

    def test_not_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/curso.html')
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'','data_fim':'','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' not in response.context)
        self.assertFormError(response, 'curso', 'data_inicio', 'Este campo é obrigatório.')
        self.assertFormError(response, 'curso', 'data_fim', 'Este campo é obrigatório.')

class CategoriaTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('criar:categoria')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/categoria.html')
        data = {'nome': 'categoria'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' in response.context)

    def test_not_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/categoria.html')
        data = {'nome': ''}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' not in response.context)
        self.assertFormError(response, 'categoria', 'nome', 'Este campo é obrigatório.')

class ModuloTestCase(TestCase):
    url_aluno = reverse('criar:aluno')
    url_categoria = reverse('criar:categoria')
    url_curso = reverse('criar:curso')

    def setUp(self):
        self.client = Client()
        self.url = reverse('criar:modulo')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/modulo.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # criando modulo
        data = {'nome': 'modulo','descricao':'descrição','is_visivel':True,'curso':1}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' in response.context)

    def test_not_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/modulo.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # criando modulo
        data = {'nome': '','descricao':'','is_visivel':True,'curso':1}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' not in response.context)
        self.assertFormError(response, 'modulo', 'nome', 'Este campo é obrigatório.')

class MaterialTestCase(TestCase):
    url_aluno = reverse('criar:aluno')
    url_categoria = reverse('criar:categoria')
    url_curso = reverse('criar:curso')
    url_modulo = reverse('criar:modulo')

    def setUp(self):
        self.client = Client()
        self.url = reverse('criar:add_material')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/aluno_curso.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # criando modulo
        data = {'nome': 'modulo','descricao':'descrição','is_visivel':True,'curso':1}
        response = self.client.post(self.url_modulo, data)
        #criando Material
        data = {'nome': 'material','modulo_atual':1,'tipo':'texto'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' in response.context)

    def test_not_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/aluno_curso.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # criando modulo
        data = {'nome': '','descricao':'','is_visivel':True,'curso':1}
        response = self.client.post(self.url_modulo, data)
        #criando Material
        data = {'nome': '','modulo_atual':1}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' not in response.context)
        self.assertFormError(response, 'aluno', 'tipo', 'Este campo é obrigatório.')
        self.assertFormError(response, 'aluno', 'nome', 'Este campo é obrigatório.')

class atividadeTestCase(TestCase):
    url_aluno = reverse('criar:aluno')
    url_categoria = reverse('criar:categoria')
    url_curso = reverse('criar:curso')
    url_modulo = reverse('criar:modulo')

    def setUp(self):
        self.client = Client()
        self.url = reverse('criar:add_atividade')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/aluno_curso.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # criando modulo
        data = {'nome': 'modulo','descricao':'descrição','is_visivel':True,'curso':1}
        response = self.client.post(self.url_modulo, data)
        #criando Material
        data = {'nome': 'material','modulo_atual':1,'tipo':'texto'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' in response.context)

    def test_not_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/aluno_curso.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # criando modulo
        data = {'nome': '','descricao':'','is_visivel':True,'curso':1}
        response = self.client.post(self.url_modulo, data)
        #criando Material
        data = {'nome': '','modulo_atual':1}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' not in response.context)
        self.assertFormError(response, 'aluno', 'tipo', 'Este campo é obrigatório.')
        self.assertFormError(response, 'aluno', 'nome', 'Este campo é obrigatório.')

class atividadeTestCase(TestCase):
    url_aluno = reverse('criar:aluno')
    url_categoria = reverse('criar:categoria')
    url_curso = reverse('criar:curso')

    def setUp(self):
        self.client = Client()
        self.url = reverse('criar:add_aluno')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/aluno_curso.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'alunos':[1,],'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # ligando o aluno ao curso
        data = {'aluno': 1,'curso':1}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' in response.context)

    def test_not_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formularios/aluno_curso.html')
        # criando aluno
        data = {'nome': 'aluno', 'email': 'fulano@fulano.com', 'telefone':'(81) sdff987456321','imagem':'dfsdgs'}
        self.client.post(self.url_aluno, data)
        # crinado categoria
        data = {'nome': 'cat'}
        response = self.client.post(self.url_categoria, data)
        # criando curso
        data = {'curso': 'python', 'professor': 'fulano','data_inicio':'01/06/2016','data_fim':'12/09/2016','descricao':'sfsdfsfsdf','sobre':'sosos','is_approved':True,'categoria':1,'imagem':''}
        self.client.post(self.url_curso, data)
        # ligando o aluno ao curso
        # teste com curso errado
        data = {'aluno': 1,'curso':0}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('sucesso' not in response.context)
        self.assertFormError(response, 'aluno', 'curso', 'Faça uma escolha válida. Sua escolha não é uma das disponíveis.')
        # teste com aluno errado
        data = {'aluno': 0,'curso':1}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'aluno', 'aluno', 'Faça uma escolha válida. Sua escolha não é uma das disponíveis.')
