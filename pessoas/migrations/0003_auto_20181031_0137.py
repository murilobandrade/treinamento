# Generated by Django 2.1.1 on 2018-10-31 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_auto_20181005_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaRn',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('pessoas.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='genero',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino')], default=0),
            preserve_default=False,
        ),
    ]
