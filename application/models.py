from django.db import models

# Create your models here.


class Categories(models.Model):
    nom_categorie = models.CharField(max_length=100)
    description_categorie = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine_categorie = f"{self.nom_categorie}. Résume : {self.description_categorie}"
        return chaine_categorie

    def dico_categorie(self):
        return {"nom_categorie" : self.nom_categorie, "description_categorie" : self.description_categorie}


class Auteurs(models.Model):
    nom_auteur = models.CharField(max_length=100)
    prenom_auteur = models.CharField(max_length=100)
    age_auteur = models.IntegerField(null = True, blank = True)
    photo_auteur = models.ImageField(upload_to='images/', null = True, blank = True)

    def __str__(self):
        chaine_auteur = f"{self.nom_auteur} {self.prenom_auteur}"
        return chaine_auteur

    def dico_auteur(self):
        return {"nom_auteur" : self.nom_auteur, "prenom_auteur" : self.prenom_auteur, "age_auteur" : self.age_auteur, "photo_auteur" : self.photo_auteur}


class Joueurs(models.Model):
    nom_joueur = models.CharField(max_length=100)
    prenom_joueur = models.CharField(max_length=100)
    mail_joueur = models.EmailField(null = True, blank = True)
    mdp_joueur = models.CharField(max_length=100, null = True, blank = True)
    PRO = 'PRO'
    PART = 'PARTICULIER'
    TYPE_JOUEUR_CHOIX = [(PRO, 'PRO'), (PART, 'PARTICULIER')]
    type_joueur = models.CharField(max_length=100, choices=TYPE_JOUEUR_CHOIX, default=PART)

    def __str__(self):
        chaine_joueur = f"{self.nom_joueur} {self.prenom_joueur}"
        return chaine_joueur

    def dico_joueur(self):
        return {"nom_joueur" : self.nom_joueur, "prenom_joueur" : self.prenom_joueur, "mail_joueur" : self.mail_joueur, "mdp_joueur" : self.mdp_joueur, "type_joueur" : self.type_joueur}


class Jeux(models.Model):
    nom_jeu = models.CharField(max_length=100)
    description_jeu = models.TextField(null = True, blank = True)
    categorie_jeu = models.ForeignKey(Categories, on_delete=models.CASCADE)
    annee_sortie_jeu = models.DateField(null = True, blank = True)
    editeur_jeu = models.CharField(max_length=100, null = True, blank = True)
    photo_jeu = models.ImageField(upload_to='media/', null = True, blank = True)
    auteur_jeu = models.ManyToManyField(Auteurs)

    def __str__(self):
        chaine_jeux = f"{self.nom_jeu}. Résume : {self.description_jeu}"
        return chaine_jeux

    def dico_jeux(self):
        return {"nom_jeux" : self.nom_jeu, "description_jeux" : self.description_jeu, "categorie_jeux" : self.categorie_jeu, "annee_sortie_jeux" : self.annee_sortie_jeu, "editeur_jeux" : self.editeur_jeu, "photo_jeux" : self.photo_jeu, "auteur_jeux" : self.auteur_jeu}


class Commentaires(models.Model):
    commentaire_jeu = models.TextField(null = True, blank = True)
    date_commentaire = models.DateField(null = True, blank = True)
    jeu_commentaire = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    joueur_commentaire = models.ForeignKey(Joueurs, on_delete=models.CASCADE)
    note_commentaire = models.IntegerField(null = True, blank = True)

    def __str__(self):
        chaine_commentaire = f"{self.commentaire_jeu}"
        return chaine_commentaire

    def dico_commentaire(self):
        return {"commentaire_jeu" : self.commentaire_jeu, "date_commentaire" : self.date_commentaire, "jeu_commentaire" : self.jeu_commentaire, "joueur_commentaire" : self.joueur_commentaire, "note_commentaire" : self.note_commentaire}
