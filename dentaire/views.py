# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dentaire import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import Group
from dentaire.forms import SignUpForm,PostForm
from django.contrib.auth.decorators import login_required
from dentaire.models import Rdv

# Create your views here.

def home(request):
	return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or none)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def rdv_new(request):
    form = PostForm (request.POST)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient=request.user.id
        rdv.id_secretaire=1
        rdv.num_rdv=1
        ####WE NEED ID_PATIENT + ID_SEC + NUMERORDV IS STATIC PROBLEM
        rdv.save()
    context = {
    'form':form,
                }

    return render(request,'panel.html',context)

class RdvForm(forms.ModelForm):
    
    class Meta:
        model = Rdv
        fields = ['date', 'num_rdv']
       
def CountNumeroRdv():
        no = Rdv.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

@login_required
def rdv_list(request, template_name='rdv_list.html'):
    if request.user.is_superuser:
        rdv = Rdv.objects.all()
    else:
        rdv = Rdv.objects.filter(id_patient=request.user.id)
    data = {}
    data['object_list'] = rdv
    return render(request, template_name, data)

@login_required
def rdv_create(request, template_name='rdv_form.html'):
    form = RdvForm(request.POST or None)


    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient=request.user
        rdv.num_rdv=CountNumeroRdv()
        rdv.save()
        return redirect('rdv_list')
    return render(request, template_name, {'form':form})

@login_required
def rdv_update(request, pk, template_name='rdv_form.html'):
    if request.user.is_superuser:
        rdv= get_object_or_404(Rdv, id=pk)
    else:
        rdv= get_object_or_404(Rdv, id=pk, id_patient=request.user)
    form = RdvForm(request.POST or None, instance=rdv)
    if form.is_valid():
        form.save()
        return redirect('rdv_list')
    return render(request, template_name, {'form':form})

@login_required
def rdv_delete(request, pk, template_name='rdv_confirm_delete.html'):
    if request.user.is_superuser:
        rdv= get_object_or_404(Rdv, id=pk)
    else:
        rdv= get_object_or_404(Rdv, id=pk, id_patient=request.user)
        print rdv
    if request.method=='POST':
        rdv.delete()
        return redirect('rdv_list')
    return render(request, template_name, {'object':rdv})

