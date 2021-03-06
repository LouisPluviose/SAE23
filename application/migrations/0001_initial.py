# Generated by Django 3.2.13 on 2022-06-10 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_auteur', models.CharField(max_length=100)),
                ('prenom_auteur', models.CharField(max_length=100)),
                ('age_auteur', models.IntegerField(blank=True, null=True)),
                ('photo_auteur', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=100)),
                ('description_categorie', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Joueurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_joueur', models.CharField(max_length=100)),
                ('prenom_joueur', models.CharField(max_length=100)),
                ('mail_joueur', models.EmailField(blank=True, max_length=254, null=True)),
                ('mdp_joueur', models.CharField(blank=True, max_length=100, null=True)),
                ('type_joueur', models.CharField(choices=[('PRO', 'PRO'), ('PARTICULIER', 'PARTICULIER')], default='PARTICULIER', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jeux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_jeu', models.CharField(max_length=100)),
                ('description_jeu', models.TextField(blank=True, null=True)),
                ('annee_sortie_jeu', models.DateField(blank=True, null=True)),
                ('editeur_jeu', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_jeu', models.ImageField(upload_to='images')),
                ('auteur_jeu', models.ManyToManyField(to='application.Auteurs')),
                ('categorie_jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire_jeu', models.TextField(blank=True, null=True)),
                ('date_commentaire', models.DateField(blank=True, null=True)),
                ('note_commentaire', models.IntegerField(blank=True, null=True)),
                ('jeu_commentaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.jeux')),
                ('joueur_commentaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.joueurs')),
            ],
        ),
    ]
