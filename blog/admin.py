from django.contrib import admin
from blog.models import Entrada,Comentario
# Register your models here.


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    pass


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass