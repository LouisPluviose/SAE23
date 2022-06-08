from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    liste_categorie = list(models.Categorie.objects.all())
    liste_auteur = list(models.Auteurs.objects.all())
    return render(request, 'application/index.html', {'liste_categorie': liste_categorie}, {'liste_auteur': liste_auteur})



def ajoutCategories(request):
    if request.GET.get("POST"):
        form = CategorieForm(request)
        if form.is_valid():
            categorie = form.save()
            return HttpResponseRedirect("/application/index")
        else:
            return render(request, "application/categorie.html", {"form": form})
    else:
        form = CategorieForm()
        return render(request, "application/categorie.html", {"form": form})


def traitementCategorie(request):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        categorie = lform.save()
        return HttpResponseRedirect("/application/index")
    else:
        return render(request, "application/categorie.html", {"form": lform})


def ajoutAuteur(request):
    if request.GET.get("POST"):
        form = AuteurForm(request)
        if form.is_valid():
            auteur = form.save()
            return HttpResponseRedirect("/application/index")
        else:
            return render(request, "application/auteur.html", {"form": form})
    else:
        form = AuteurForm()
        return render(request, "application/auteur.html", {"form": form})


def traitementAuteur(request):
    lform = AuteurForm(request.POST)
    if lform.is_valid():
        auteur = lform.save()
        return HttpResponseRedirect("/application/index")
    else:
        return render(request, "application/auteur.html", {"form": lform})