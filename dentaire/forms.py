from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dentaire.models import Rdv
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets                                       
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class PostForm(forms.ModelForm):

    class Meta:
        model = Rdv
        fields = ['date',]
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['date'].widget.attrs['class'] = 'datepicker'


# class RdvCreateForm(forms.ModelForm):
# 		class Meta:
# 				model = Rdv
# 			   exclude = ('id_secretaire',)
# 		def __init__(self, *args, **kwargs):
# 				self.request = kwargs.pop('request', None)
# 				super(RdvCreateForm, self).__init__(*args, **kwargs)

# class RdvUpdateForm(forms.ModelForm):
# 		class Meta:
# 				model = Rdv
		

# 		def __init__(self, *args, **kwargs):
# 				self.request = kwargs.pop('request', None)
# 				super(RdvUpdateForm, self).__init__(*args, **kwargs)




