
from django.contrib import admin
from .models import Usuario, Sala, Chave, Autorizacao, Posse, StatusGeral

admin.site.register(Usuario)
admin.site.register(Sala)
admin.site.register(Chave)
admin.site.register(Autorizacao)
admin.site.register(Posse)
admin.site.register(StatusGeral)
