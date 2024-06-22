from django.urls import path
from . import views

urlpatterns=[
    path('fun201/',views.fun201,name='fun201'),
    path('fun202/',views.fun202,name='fun202'),
    path('fun203/',views.fun203,name='fun203'),
]