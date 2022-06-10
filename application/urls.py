from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('categorie/', views.ajoutCategories, name='ajoutCategories'),
    path('traitementCategorie/', views.traitementCategorie, name='traitementCategories'),
    path('afficheCategorie/', views.afficheCategorie, name='afficheCategorie'),
    path('auteur/', views.ajoutAuteur, name='ajoutAuteur'),
    path('traitementAuteur/', views.traitementAuteur, name='traitementAuteur'),
    path('afficheAuteur/', views.afficheAuteur, name='afficheAuteur'),
    path('joueur/', views.ajoutJoueur, name='ajoutJoueur'),
    path('traitementJoueur/', views.traitementJoueur, name='traitementJoueur'),
    path('afficheJoueur/', views.afficheJoueur, name='afficheJoueur'),
    path('jeu/', views.ajoutJeu, name='ajoutJeux'),
    path('traitementJeu/', views.traitementJeu, name='traitementJeux'),
    path('afficheJeu/', views.afficheJeu, name='afficheJeux'),
]