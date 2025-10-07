from django.contrib import admin
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda", "publicada") #* oq aparece no display do site
    list_display_links = ("id","nome") #* os links que levam a edicao
    search_fields = ("nome",) #* cria uma busca
    list_filter = ("categoria", "usuario") #* cria um filtro
    list_editable = ("publicada",)
    list_per_page = 10
    

admin.site.register(Fotografia, ListandoFotografias)
