from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista, name='lista'),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
]