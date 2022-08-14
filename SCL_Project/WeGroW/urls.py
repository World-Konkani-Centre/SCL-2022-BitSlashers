from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='WeGroW-home'),
    path('home/', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('service-detail/', views.service_detail, name='service-detail'),
    path('view_store/', views.view_store, name='view_store'),
    path('sell/', views.sell, name='sell'),
    path('buy/', views.buy, name='buy'),
    path('login/', views.loginp, name='login'),
    path('signup/', views.signup, name='signup'),
    path('otp/', views.otp, name='otp'),
    path('invalid/',views.invalid,name='invalid'),
    path('logout/', views.my_logout, name='logout'),
    path('buyer/', views.buyer, name='buyer'),
    path('profile/', views.profile, name='profile'),
    path('user_analytics/', views.user_analytics, name='user_analytics'),
    path('option/', views.option, name='option'),
    path('confirm/', views.confirm, name='confirm'),
    path('trend/', views.trend, name='trend'),
    path('confirm-buy/',views.confirmBuy,name='confirm-buy'),
    path('analytics_option/', views.analyticsOption, name='analytics_option'),
    path('analytics_bought/', views.analyticsBought, name='analytics_bought'),
    path('analytics_sold/', views.analyticsSold, name='analytics_sold'),
    path('analytics_for_sale/', views.analyticsForSale, name='analytics_for_sale'),

]
