from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from . import models


class CategorieForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = {'nom_categorie', 'description_categorie'}
        labels = {
            'nom_categorie': _('Nom de la catégorie'),
            'description_categorie': _('Description de la catégorie'),
        }


class AuteurForm(ModelForm):
    class Meta:
        model = models.Auteurs
        fields = {'nom_auteur', 'prenom_auteur', 'age_auteur', 'photo_auteur'}
        labels = {
            'nom_auteur': _('Nom de l\'auteur'),
            'prenom_auteur': _('Prénom de l\'auteur'),
            'age_auteur': _('Age de l\'auteur'),
            'photo_auteur': _('Photo de l\'auteur'),
        }


class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueurs
        fields = {'nom_joueur', 'prenom_joueur', 'mail_joueur', 'mdp_joueur', 'type_joueur'}
        labels = {
            'nom_joueur': _('Nom du joueur'),
            'prenom_joueur': _('Prénom du joueur'),
            'mail_joueur': _('Mail du joueur'),
            'mdp_joueur': _('Mot de passe du joueur'),
            'type_joueur': _('Type de joueur'),
        }


class JeuForm(ModelForm):
    class Meta:
        model = models.Jeux
        fields = {'nom_jeu', 'description_jeu', 'categorie_jeu', 'annee_sortie_jeu', 'editeur_jeu', 'photo_jeu', 'auteur_jeu'}
        labels = {
            'nom_jeu': _('Nom du jeu'),
            'description_jeu': _('Description du jeu'),
            'categorie_jeu': _('Catégorie du jeu'),
            'annee_sortie_jeu': _('Année de sortie du jeu'),
            'editeur_jeu': _('Editeur du jeu'),
            'photo_jeu': _('Photo du jeu'),
            'auteur_jeu': _('Auteur du jeu'),
        }


class CommentaireForm(ModelForm):
    class Meta:
        model = models.Commentaires
        fields = {'commentaire_jeu', 'date_commentaire', 'jeu_commentaire', 'joueur_commentaire', 'note_commentaire'}
        labels = {
            'commentaire_jeu': _('Commentaire du jeu'),
            'date_commentaire': _('Date du commentaire'),
            'jeu_commentaire': _('Jeu du commentaire'),
            'joueur_commentaire': _('Joueur du commentaire'),
            'note_commentaire': _('Note du commentaire'),
        }

