from datetime import date, datetime

from django.db import models

# Create your models here.
class PessoaClasse:
    def set_nome(self, nome_informado):
        self.nome = nome_informado

    def set_nascimento(self, data_nascimento: date = 10) -> bool:
        print(data_nascimento)
        data_atual = datetime.now()
        self.data_nascimento = data_atual
        if not isinstance(data_nascimento, date):
            raise Exception("Conteudo invalido (esperado: data)")

        if data_atual.year < data_nascimento.year:
            raise Exception("Não é possivel nascer no futuro")

        self.data_nascimento = data_nascimento

    def calcular_idade(self):
        """
        Essa funcao ira calcular a idade do fulaninho com base na data atual
        
        return: uma idade
        """
        datetime_atual = datetime.now()
        ano_atual = datetime_atual.year
        return ano_atual - self.data_nascimento.year


class Pessoa(models.Model):
    nome = models.CharField(blank=False, max_length=50)
    data_nascimento = models.DateField(blank=False)
    apelido = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=20)


    # def __init__(self, nome_pessoa: str, data_nascimento: date):
    #     self.nome = nome_pessoa

    #     data_atual = datetime.now()
    #     self.data_nascimento = data_atual
    #     if not isinstance(data_nascimento, date):
    #         raise Exception("Conteudo invalido (esperado: data)")

    #     if data_atual.year < data_nascimento.year:
    #         raise Exception("Não é possivel nascer no futuro")

    #     self.data_nascimento = data_nascimento

    def calcular_idade(self):
        """
        Essa funcao ira calcular a idade do fulaninho com base na data atual
        
        return: uma idade
        """
        datetime_atual = datetime.now()
        ano_atual = datetime_atual.year
        return ano_atual - self.data_nascimento.year


# objeto_pessoa = Pessoa()
# objeto_pessoa.set_nome("Nayara")
# objeto_pessoa.set_nascimento("1123123")
# print(objeto_pessoa.nome)
# print(objeto_pessoa.data_nascimento)

# print(objeto_pessoa.calcular_idade())