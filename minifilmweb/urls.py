from django.urls import path
from .views import filmy, nowy_film, edytuj_film, usun_film



urlpatterns = [
    path('filmy/',filmy, name="filmy"),
    path('nowy/',nowy_film, name="nowy_film"),
    path('edytuj/<int:id>',edytuj_film, name="edytuj_film"),
    path('usun/<int:id>',usun_film, name="usun_film"),
]
