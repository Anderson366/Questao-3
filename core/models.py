from django.db import models


# Create your models here.
class ItemTema(models.Model):
    cod_item = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=20)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = 'ItensTemas'
        verbose_name = 'ItemTema'


class Tema(models.Model):
    cod_tema = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=20)
    valor_aluguel = models.FloatField()
    cor_toalha = models.CharField(max_length=20)
    cod_item = models.ForeignKey(ItemTema, on_delete=models.CASCADE, )

    class Meta:
        verbose_name_plural = 'Temas'
        verbose_name = 'Tema'

class Endereco(models.Model):
    cod_endere = models.IntegerField(primary_key=True)
    logradouro = models.CharField(max_length=30)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=40)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = 'Enderecos'
        verbose_name = 'Endereco'


class Cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True)
    nome = models.CharField('Cliente:', max_length=40)
    telefone = models.CharField(max_length=11)

    class Meta:
        verbose_name_plural = 'Clientes'
        verbose_name = 'Cliente'


class Aluguel(models.Model):
    cod_aluguel = models.IntegerField(primary_key=True)
    data_festa = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    valor_cobrado = models.FloatField()
    cod_tema = models.ForeignKey(Tema, on_delete=models.CASCADE, )
    cod_endere = models.ForeignKey(Endereco, on_delete=models.CASCADE, )
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, )


    class Meta:
        verbose_name_plural = 'Alugueis'
        verbose_name = 'Aluguel'