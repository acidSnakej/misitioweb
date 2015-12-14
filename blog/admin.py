from django.contrib import admin
from blog.models import Entrada
# Register your models here.


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    pass
