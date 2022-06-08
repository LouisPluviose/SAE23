from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('categorie/', views.ajoutCategories, name='ajoutCategories'),
    path('traitementCategorie/', views.traitementCategorie, name='traitementCategories'),
]