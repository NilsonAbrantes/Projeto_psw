from django.contrib import admin

from .models import PedidosExames, SolicitacaoExame, TipoExames

admin.site.register(TipoExames)
admin.site.register(SolicitacaoExame)
admin.site.register(PedidosExames)
