# -*- coding: latin-1 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Projet(models.Model):
    """
    Objet qui rassemble toutes les informations relatives à un Projet
    C'est à dire :
                    - id : identifiant unique (généré autaomatiquement par Django)
    				- date_debut : la date de lancement du projet
    				- nom : le nom du Projet
    				- descriptif : description du projet
    				- en_cours : si le projet est en cours ou non
    				- nom_client : le nom du client
    				- responsable : l'utilisateur responsable
    """
    date_debut = models.DateField('Date publiee',auto_now=True,help_text="la date à laquelle le projet a debute")
    nom = models.CharField(max_length=400,help_text="nom du projet")
    descriptif = models.CharField(max_length=8000,help_text="informations relatives au document")
    en_cours = models.BooleanField(default=True, help_text="état du projet, si il est en cours ou non")
    nom_client = models.CharField(max_length=400,help_text="le nom du client principal du projet")
    responsable = models.ForeignKey(User)


class Document(models.Model):
    """
    Objet qui rasemble les informations d'un document utilise au sein de l'application.
    C'est à dire :
                 - id : identifiant unique (généré automatiquement par Django)
    			 - date_publiee : la date correspondant a son entree dans la base de donnee
    			 - proprietaire : l'utilisateur qui a rentre le document au sein du systeme
    			 - commentaire : les informations relatives au documents saisie par l'utilisateur

    """
    fichier = models.FileField(upload_to='doc/')
    date_publiee = models.DateField('Date publiee',auto_now=True,help_text="La date a laquelle le document a ete integre au systeme")
    proprietaire = models.ForeignKey(User)
    descriptif = models.CharField(max_length=8000,help_text="informations relatives au document")
    commentaire = models.CharField(max_length=8000,help_text="commentaires sur document")
    projet = models.ForeignKey(Projet)

class Exigence(models.Model):
    """
    Objet qui rassemble toutes les informations relatives à une éxigences.
    C'est à dire :
                 - id : identifiant unique (généré autaomatiquement par Django)
                 - description : la description de l'éxigence
                 - commentaire : commentaire sur l'exigence
                 - projet : le projet auquel
    """
    commentaire = models.CharField(max_length=8000,help_text="informations relatives a l'exigence")
    descriptif = models.CharField(max_length=8000,help_text="description de l'exigence")
    projet = models.ForeignKey(Projet)
    priorite = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])