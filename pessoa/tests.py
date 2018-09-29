from datetime import date, datetime

from django.test import TestCase, Client

from pessoa.models import PessoaClasse, Pessoa

# Create your tests here.

class HelloWorld(TestCase):
    def test_hello_world(self):
        # Construçao do cenario
        retorno = "Hello World"

        # Execução 
        pass

        # Validações
        # Isso aqui deve retornar True
        self.assertTrue(True)
        self.assertEquals("Hello World", retorno)


class HelloWorldClient(TestCase):
    def test_view_hello_world(self):
        # Construção Cenario
        client = Client()

        # Execução
        retorno = client.get("/pessoa/hello")

        # Validação (test)
        self.assertEquals(200, retorno.status_code)
        self.assertEquals(b"Hello World", retorno.content)


class TestPessoaModel(TestCase):
    def test_nascimento_pessoa(self):
        """
        Verifica a data de nascimento de uma pessoa nascida em 1991
        """
        # Construção Cenario
        objeto_pessoa = PessoaClasse()
        data_murilo = date(1991, 2, 27)

        # Execução
        objeto_pessoa.set_nome("Murilo")
        objeto_pessoa.set_nascimento(data_murilo)

        idade = objeto_pessoa.calcular_idade()

        # Validação
        self.assertEquals(27, idade)

    def test_nascimento_pessoa_futuro(self):
        """
        Verificação de uma pessoa nascida no futuro
        """
        # Construção Cenario
        data_atual = datetime.now()
        objeto_pessoa = PessoaClasse()
        data_murilo = date(data_atual.year + 1, 2, 27)

        # Execução
        objeto_pessoa.set_nome("Murilo")

        with self.assertRaises(Exception):
            self.assertEquals(None, objeto_pessoa.set_nascimento(data_murilo))
            # self.assertEquals(, str(erro))

        # try:
        #     objeto_pessoa.set_nascimento(data_murilo)
        #     self.fail()
        # except Exception as erro:
        #     # Validação
        #     self.assertEquals("Não é possivel nascer no futuro", str(erro))
        

        # self.assertFalse(retorno)

    def test_model_pessoa(self):
        """
        Verificação da criacaoa de uma model pessoa
        """
        # Construção Cenario
        data_atual = datetime.now()
        objeto_pessoa = Pessoa("Murilo", date(1991, 2, 27))
        self.assertEquals("Murilo", objeto_pessoa.nome)
        self.assertEquals(date(1991, 2, 27), objeto_pessoa.data_nascimento)
