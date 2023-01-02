from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]