from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='WeGroW-home'),
    path('home/', views.home, name='index'),
    path('store/', views.store, name='store'),

]
