from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('katalog', views.katalog, name='katalog'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('create_about', views.create_about, name='create_about'),
]
