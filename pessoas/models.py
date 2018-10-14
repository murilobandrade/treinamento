from django.db import models


class Pessoa(models.Model):
    ESTADO_CIVIL_CHOICES = (
        (1, u'Solteiro'),
        (2, u'Casado'),
        (3, u'Separado'),
        (4, u'Divorciado'),
        (5, u'Viúvo')
    )

    nome = models.CharField(blank=False, max_length=50)
    data_nascimento = models.DateField(blank=False)
    apelido = models.CharField(max_length=20)
    estado_civil = models.IntegerField(
        choices=ESTADO_CIVIL_CHOICES
    )
