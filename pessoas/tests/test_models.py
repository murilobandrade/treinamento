from datetime import date, datetime

from django.test import TestCase, Client

from .models import Pessoa
from .services import calculate_years_old


class TestService(TestCase):
    def test_calculate_year_old(self):
        birth_date = date(1991, 2, 27)

        years_old = calculate_years_old(birth_date)

        self.assertEquals(27, years_old)


class TestPessoaModel(TestCase):
    def test_model_pessoa(self):
        """
        Verificação da criacaoa de uma model pessoa
        """
        # Construção Cenario
        data_atual = datetime.now()
        objeto_pessoa = Pessoa("Murilo", date(1991, 2, 27))
        self.assertEquals("Murilo", objeto_pessoa.nome)
        self.assertEquals(date(1991, 2, 27), objeto_pessoa.data_nascimento)
