from django.contrib import admin

from .models import Ingredientes, Receta, Preparacion, Peso


admin.site.register(Ingredientes)
admin.site.register(Receta)
admin.site.register(Preparacion)
admin.site.register(Peso)
