from django.urls import path
from MeuApp import views


#Registrar as urls do app

#qual url corresponde a cada view

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('produtos/', views.exibir_produtos, name= 'produto'),
]
