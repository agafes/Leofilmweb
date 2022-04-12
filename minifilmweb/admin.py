from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ['tytul','rok','opis','plakat']
    exclude = ['premiera']
    list_display = ['tytul','rok','imdb_rating']
    list_filter = ['rok']
    search_fields = ['tytul','opis']

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)

