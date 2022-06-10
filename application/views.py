from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from . import models

# Create your views here.


def index(request):
    return render(request, 'application/index.html')



def ajoutCategories(request):
    if request.GET.get("POST"):
        form = CategorieForm(request)
        if form.is_valid():
            categorie = form.save()
            return HttpResponseRedirect("/application/affichecategorie")
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


def afficheCategorie(request):
    liste_categorie = list(models.Categories.objects.all())
    return render(request, "application/affichecategorie.html", {"liste_categorie": liste_categorie})


def ajoutAuteur(request):
    if request.GET.get("POST"):
        form = AuteurForm(request.POST, request.FILES)
        if form.is_valid():
            auteur = form.save()
            return HttpResponseRedirect("/application/afficheauteur")
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


def afficheAuteur(request):
    liste_auteur = list(models.Auteurs.objects.all())
    return render(request, "application/afficheauteur.html", {"liste_auteur": liste_auteur})


def ajoutJoueur(request):
    if request.GET.get("POST"):
        form = JoueurForm(request.POST)
        if form.is_valid():
            joueur = form.save()
            return HttpResponseRedirect("/application/affichejoueur")
        else:
            return render(request, "application/joueur.html", {"form": form})
    else:
        form = JoueurForm()
        return render(request, "application/joueur.html", {"form": form})


def traitementJoueur(request):
    lform = JoueurForm(request.POST)
    if lform.is_valid():
        joueur = lform.save()
        return HttpResponseRedirect("/application/index")
    else:
        return render(request, "application/joueur.html", {"form": lform})


def afficheJoueur(request):
    liste_joueur = list(models.Joueurs.objects.all())
    return render(request, "application/affichejoueur.html", {"liste_joueur": liste_joueur})


def ajoutJeu(request):
    if request.GET.get("POST"):
        form = JeuForm(request.POST, request.FILES)
        if form.is_valid():
            jeu = form.save()
            return HttpResponseRedirect("/application/affichejeu")
        else:
            return render(request, "application/jeu.html", {"form": form})
    else:
        form = JeuForm()
        return render(request, "application/jeu.html", {"form": form})


def traitementJeu(request):
    lform = JeuForm(request.POST)
    if lform.is_valid():
        jeu = lform.save()
        return HttpResponseRedirect("/application/index")
    else:
        return render(request, "application/jeu.html", {"form": lform})


def afficheJeu(request):
    liste_jeu = list(models.Jeux.objects.all())
    return render(request, "application/affichejeu.html", {"liste_jeu": liste_jeu})


def ajoutCommentaire(request):
    if request.GET.get("POST"):
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save()
            return HttpResponseRedirect("/application/affichecommentaire")
        else:
            return render(request, "application/commentaire.html", {"form": form})
    else:
        form = CommentaireForm()
        return render(request, "application/commentaire.html", {"form": form})


def traitementCommentaire(request):
    lform = CommentaireForm(request.POST)
    if lform.is_valid():
        commentaire = lform.save()
        return HttpResponseRedirect("/application/index")
    else:
        return render(request, "application/commentaire.html", {"form": lform})


def afficheCommentaire(request):
    liste_commentaire = list(models.Commentaires.objects.all())
    return render(request, "application/affichecommentaire.html", {"liste_commentaire": liste_commentaire})