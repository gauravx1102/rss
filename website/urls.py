from django.urls import path
from unicodedata import name
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('ask_your_query/', views.ask_your_query, name='ask_your_query'),
    path('send_email/', views.send_email, name='send_email'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about_us, name='about_us'),
]
