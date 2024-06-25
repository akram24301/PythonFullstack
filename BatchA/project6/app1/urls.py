from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('display_cr/',views.display_cr,name='display_cr'),
]