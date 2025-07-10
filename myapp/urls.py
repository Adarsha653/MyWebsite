from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]