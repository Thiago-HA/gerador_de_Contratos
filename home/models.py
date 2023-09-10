from datetime import date
from django.db import models

class Contrato(models.Model):
    descricao = models.CharField("Descrição",max_length=100, blank=False, null=False)
    nome_contratante = models.CharField("Nome do contratante",max_length=100, blank=False, null=False)
    cpf_contratante = models.CharField("CPF do contratante",max_length=100, blank=False, null=False)
    rua_contratante = models.CharField("Rua do contratante",max_length=100, blank=False, null=False)
    numero_contratante = models.CharField("Número do contratante",max_length=100, blank=False, null=False)
    cidade_contratante = models.CharField("Cidade do contratante",max_length=100, blank=False, null=False)
    estado_contratante = models.CharField("Estado do contratante",max_length=100, blank=False, null=False)
    salao = models.CharField("Salão",max_length=100, blank=False, null=False)
    evento = models.CharField("Tipo do Evento",max_length=100, blank=False, null=False)
    qtd_convidados = models.IntegerField("Quantidade de convidados",max_length=10, blank=False, null=False)
    data_evento = models.CharField("Data do Evento",max_length=100, blank=False, null=False)
    qtd_garcons = models.IntegerField("Quantidade de garçons",max_length=10, blank=False, null=False)
    valor = models.DecimalField("Valor do Aluguel", max_digits=8, decimal_places=2, blank=False, null=False)
    valor_buffet = models.DecimalField("Valor do Buffet", max_digits=8, decimal_places=2, blank=False, null=False)
    data_pagar = models.DateTimeField("Data a pagar", auto_now=False, auto_now_add=False, blank=False, null=False)
    data_contrato = models.DateTimeField("Data do contrato", default= date.today)

    class Meta:
        verbose_name = 'Contratos'

    def __str__(self) -> str:
        return self.descricao