from django.contrib import admin
from django.urls import path, include
from profesional.views import home_professional,datos_pro

urlpatterns = [
    path('profesional/', home_professional, name='home-prof'),
    path('profesional/datos/', datos_pro, name='datos-prof'),

]