from django.contrib import admin
from .models import Marca, Veiculo, Pessoa, movRotativo, Mensalista, MovMensalista

class movRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin','checkout', 'valor_hora',
                    'horas_total', 'total', 'veiculo', 'pago')

    def veiculo(self, obj):
        return obj.veiculo
    
class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista','dt_pgto','total')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(movRotativo, movRotativoAdmin)