from django.db import models


class Pessoa(models.Model):
    ESTADO_CIVIL_SOLTEIRO = 1
    ESTADO_CIVIL_CASADO = 2
    ESTADO_CIVIL_SEPARADO = 3
    ESTADO_CIVIL_DIVORCIADO = 4
    ESTADO_CIVIL_VIUVO = 5
    ESTADO_CIVIL_CHOICES = (
        (ESTADO_CIVIL_SOLTEIRO, u'Solteiro'),
        (ESTADO_CIVIL_CASADO, u'Casado'),
        (ESTADO_CIVIL_SEPARADO, u'Separado'),
        (ESTADO_CIVIL_DIVORCIADO, u'Divorciado'),
        (ESTADO_CIVIL_VIUVO, u'Viúvo')
    )

    GENERO_MASCULINO = 1
    GENERO_FEMINIO = 2
    GENERO_CHOICES = (
        (GENERO_MASCULINO, u'Masculino'),
        (GENERO_FEMINIO, u'Feminino')
    )

    nome = models.CharField(blank=False, max_length=50)
    data_nascimento = models.DateField(blank=False)
    apelido = models.CharField(max_length=20)
    estado_civil = models.IntegerField(
        choices=ESTADO_CIVIL_CHOICES
    )
    genero = models.IntegerField(
        choices=GENERO_CHOICES
    )
