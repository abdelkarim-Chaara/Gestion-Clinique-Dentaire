# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dentaire.models import FichePatient,CabinetDentaire,Rdv,Consultation,Facture,Ordonnance
from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User



# Register your models here.


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'first_name', 'last_name')
#     list_filter = ('is_staff', 'is_superuser')


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
#altering defaut form to make passwod input hidden 
# class UtilisateurForm(ModelForm):
# 	password = forms.CharField(widget=PasswordInput())
# 	# role_list = ['utilisateur','medecine','secretaire','admin']
# 	# role = forms.ChoiceField(choices=role_list)
# 	class Meta:
# 		model = Utilisateur
# 		exclude = ()

# class UtilisateurUserAdmin(admin.ModelAdmin):
# 	form = UtilisateurForm

# admin.site.register(Utilisateur,UtilisateurUserAdmin)
admin.site.register(CabinetDentaire)
admin.site.register(FichePatient)
admin.site.register(Rdv)
admin.site.register(Consultation)
admin.site.register(Facture)
admin.site.register(Ordonnance)

