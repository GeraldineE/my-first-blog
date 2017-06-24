from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #Se asigna una vista vista view llamada post_list a la URL ^$
       url(r'^$', views.post_list, name='post_list'),

]
