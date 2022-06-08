from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)
    decription_categorie = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine_categorie = f"{self.nom_categorie}. Résume : {self.decription_categorie}"
        return chaine_categorie

    def dico_categorie(self):
        return {"nom_categorie" : self.nom_categorie, "decription_categorie" : self.decription_categorie}


class auteurs(models.Model):
    nom_auteur = models.CharField(max_length=100)
    prenom_auteur = models.CharField(max_length=100)
    age_auteur = models.IntegerField(null = True, blank = True)
    photo_auteur = models.ImageField(upload_to='images/', null = True, blank = True)

    def __str__(self):
        chaine_auteur = f"{self.nom_auteur} {self.prenom_auteur}"
        return chaine_auteur

    def dico_auteur(self):
        return {"nom_auteur" : self.nom_auteur, "prenom_auteur" : self.prenom_auteur, "date_naissance_auteur" : self.date_naissance_auteur, "date_deces_auteur" : self.date_deces_auteur}


class Jeux(models.Model):
    nom_jeux = models.CharField(max_length=100)
    description_jeux = models.TextField(null = True, blank = True)
    categorie_jeux = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    annee_sortie_jeux = models.DateField(null = True, blank = True)
    editeur_jeux = models.CharField(max_length=100, null = True, blank = True)
    photo_jeux = models.ImageField(upload_to='images/', null = True, blank = True)
    auteur_jeux = models.ManyToManyField(auteurs)

    def __str__(self):
        chaine_jeux = f"{self.nom_jeux}. Résume : {self.description_jeux}"
        return chaine_jeux

    def dico_jeux(self):
        return {"nom_jeux" : self.nom_jeux, "description_jeux" : self.description_jeux, "categorie_jeux" : self.categorie_jeux}


class Joueur(models.Model):
    nom_joueur = models.CharField(max_length=100)
    prenom_joueur = models.CharField(max_length=100)
    age_joueur = models.IntegerField(null = True, blank = True)
    photo_joueur = models.ImageField(upload_to='images/', null = True, blank = True)
    jeux_joueur = models.ManyToManyField(Jeux)

    def __str__(self):
        chaine_joueur = f"{self.nom_joueur} {self.prenom_joueur}"
        return chaine_joueur

    def dico_joueur(self):
        return {"nom_joueur" : self.nom_joueur, "prenom_joueur" : self.prenom_joueur, "date_naissance_joueur" : self.date_naissance_joueur, "date_deces_joueur" : self.date_deces_joueur}