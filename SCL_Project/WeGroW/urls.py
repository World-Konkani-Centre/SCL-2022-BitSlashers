from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='WeGroW-home'),
    path('home/', views.home, name='index'),
    path('about/', views.about, name='about'),

]
