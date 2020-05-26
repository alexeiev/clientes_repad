from django.db import models

class ClassificacaoCliente(models.Model):
    classificacao = models.CharField(max_length=15)
     
    def __str__(self):
        return self.classificacao

class Cliente(models.Model):
    sigla = models.CharField(max_length=20)
    nome_cliente = models.CharField(max_length=100)
    responsavel_administrativo = models.CharField(max_length=60)
    administrativo_telefone = models.CharField(max_length=12)
    administrativo_email = models.CharField(max_length=50)
    responsavel_tecnico = models.CharField(max_length=60)
    tecnico_telefone = models.CharField(max_length=12)
    tecnico_email = models.CharField(max_length=50)
    classificacao = models.ForeignKey('ClassificacaoCliente', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cliente


class Site(models.Model):
    nome_site = models.CharField(max_length=100)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    endereco = models.CharField(max_length=150)
    cep = models.CharField(max_length=10)
    link_ip = models.CharField(max_length=8, null=True, blank=True)
    lan_to_lan = models.CharField(max_length=8, null=True, blank=True)
    vpn_l3 = models.CharField(max_length=8, null=True, blank=True)
    bloco_ip = models.CharField(max_length=5, null=True, blank=True)
    data_ativacao = models.DateField(verbose_name='Ativação')
    status = models.BooleanField(verbose_name='Status', default=True)
    
    def __str__(self):
        return self.nome_site

