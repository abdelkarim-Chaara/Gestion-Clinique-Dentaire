"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from dentaire.views  import home,signup,rdv_list,rdv_create,rdv_update,rdv_delete
from django.contrib.auth import views as auth_views
admin.site.site_header = 'Clinique Dentaire Administration'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home,name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^crud/',  include('crudbuilder.urls')),

    #url(r'^panel$', rdv_new, name='rdv_new'),

  url(r'^panel$', rdv_list, name='rdv_list'),
  url(r'^new$',rdv_create, name='rdv_new'),
  url(r'^edit/(?P<pk>\d+)$', rdv_update, name='rdv_edit'),
  url(r'^delete/(?P<pk>\d+)$', rdv_delete, name='rdv_delete'),


]