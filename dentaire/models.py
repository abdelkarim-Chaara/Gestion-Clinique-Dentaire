# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

# class Medecin (Utilisateur):
# 	    id_medecin = models.AutoField(primary_key=True)
# 		id_utilisateur = models.ForeignKey('Utilisateur',on_delete=models.CASCADE)
		
# class Administrateur (Utilisateur):
# 	    id_admin = models.AutoField(primary_key=True)
# 		id_utilisateur = models.ForeignKey('Utilisateur',on_delete=models.CASCADE,)
		
# class Secretaire (Utilisateur):
# 	    id_secretaire = models.AutoField(primary_key=True)
# 		id_utilisateur = models.ForeignKey('Utilisateur',on_delete=models.CASCADE, )
			

# class Patient (Utilisateur):
# 		id_patient = models.AutoField(primary_key=True)	
# 		id_utilisateur = models.ForeignKey('Utilisateur',on_delete=models.CASCADE, )
# 		id_cabinet = models.ForeignKey('CabinetDentaire',on_delete=models.CASCADE, )
# 		id_rdv = models.ForeignKey('Rdv',on_delete=models.CASCADE, )

# class Utilisateur (models.Model):
# 	id_utilisateur = models.AutoField(primary_key=True)
# 	login = models.CharField(max_length=254)
# 	password = models.CharField(max_length=254)
# 	nom = models.CharField(max_length=254)
# 	prenom = models.CharField(max_length=254)
# 	tel = PhoneNumberField(blank=True)
# 	address = models.CharField(max_length=254)
# 	email 	= models.EmailField()
# 	#role = models.CharField(default='utilisateur',max_length=254)
# 	def __str__ (self):
# 		return str(self.login)

## full_name = '%s %s' % (self.first_name, self.last_name)
## return full_name.strip()
class CabinetDentaire (models.Model):
		id_cabinet = models.AutoField(primary_key=True)
		intitule = models.CharField(max_length=254)
		address = models.CharField(max_length=254)
		email= models.EmailField()
		tel = PhoneNumberField(blank=True)
		fax =  PhoneNumberField(blank=True)
		def __str__ (self):
		 return str(self.intitule)

class Rdv (models.Model):
	id = models.AutoField(primary_key=True)
	id_secretaire = models.ForeignKey(User,related_name="rdv_sec",on_delete=models.CASCADE,default="3", )
	id_patient = models.ForeignKey(User,related_name="rdv_patient",on_delete=models.CASCADE,default="4" )
	date = models.DateTimeField()

	num_rdv = models.IntegerField(default="1")
	def __str__ (self):
		return str(self.id_patient.username)

class FichePatient (models.Model):
	id_fiche = models.AutoField(primary_key=True)
	id_patient = models.ForeignKey(User,related_name="fich_patient",on_delete=models.CASCADE, )
	id_secretaire = models.ForeignKey(User,related_name="fich_sec",on_delete=models.CASCADE, )
	nom = models.CharField(max_length=254)
	prenom = models.CharField(max_length=254)
	address = models.CharField(max_length=254)
	age=models.IntegerField()
	sexe=models.CharField(max_length=254)
	tel = PhoneNumberField(blank=True)
	email 	= models.EmailField()
	CNAM = models.CharField(max_length=254)
	profession = models.CharField(max_length=254)
	motif_consultation = models.CharField(max_length=254)
	def __str__ (self):
		return str(self.id_patient.username)
class Consultation (models.Model):
	id_consultation = models.AutoField(primary_key=True)
	id_medecin = models.ForeignKey(User,related_name="cons_medecine",on_delete=models.CASCADE, )
	id_patient = models.ForeignKey(User,related_name="cons_patient",on_delete=models.CASCADE, )
	id_facture = models.ForeignKey('Facture',related_name="cons_fact",on_delete=models.CASCADE, )
	contenue = models.TextField(max_length=254)
	antecedant = models.CharField(max_length=254)
	traitement = models.CharField(max_length=254)
	date_consultation = models.DateTimeField()
	def __str__ (self):
		return str(self.id_patient.username)
class Facture (models.Model):
	id_facture = models.AutoField(primary_key=True)
	#id_consultation = models.ForeignKey('Consultation',related_name="facture_consultation",on_delete=models.CASCADE, )
	prix = models.FloatField()
	date = models.DateTimeField()
	def __str__ (self):
		return str(self.date)
class Ordonnance (models.Model):
	id_ordonnance = models.AutoField(primary_key=True)
	#date = models.DateTimeField(auto_now_add=True, blank=True)
	date = models.DateTimeField()
	medicament = models.CharField(max_length=254)
	observation = models.CharField(max_length=254)
	def __str__ (self):
		return str(self.date)



