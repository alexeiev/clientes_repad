from django.contrib import admin
from core.models import Site, Cliente, ClassificacaoCliente

# Register your models here.

class SitesCliente(admin.ModelAdmin):
    list_display = ('cliente', 'nome_site', 'link_ip', 'lan_to_lan', 'vpn_l3', 'bloco_ip', 'data_ativacao')
    list_filter = ('cliente', 'link_ip', 'lan_to_lan', 'vpn_l3', 'bloco_ip')

admin.site.register(Site, SitesCliente)
admin.site.register(Cliente)
admin.site.register(ClassificacaoCliente)

