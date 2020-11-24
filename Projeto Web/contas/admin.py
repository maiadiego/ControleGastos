from django.contrib import admin
from .models import Categoria
from .models import Transacao
# Registrar os models
admin.site.register(Categoria)
admin.site.register(Transacao)
