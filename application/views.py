from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'application/index.html', {'liste': liste})


def categorie(request):
    return render(request, 'application/categorie.html')


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