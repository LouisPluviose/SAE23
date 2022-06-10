from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('categorie/', views.ajoutCategories, name='ajoutCategories'),
    path('traitementCategorie/', views.traitementCategorie, name='traitementCategories'),
    path('afficheCategorie/', views.afficheCategorie, name='afficheCategorie'),
    path('auteur/', views.ajoutAuteur, name='ajoutAuteur'),
    path('traitementAuteur/<int:id>', views.traitementAuteur, name='traitementAuteur'),
    path('afficheAuteur/', views.afficheAuteur, name='afficheAuteur'),
]