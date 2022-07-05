from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='WeGroW-home'),
    path('home/', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('service-detail/', views.service_detail, name='service-detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('add-store/', views.add_store, name='store'),

]