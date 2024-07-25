from django.contrib import admin
from aluraflix.models import Video, Categoria

# Register your models here.

class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo','categoria')
    list_per_page = 20

admin.site.register(Video, Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20

admin.site.register(Categoria, Categorias)