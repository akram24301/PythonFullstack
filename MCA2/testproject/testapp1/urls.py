from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun101,name='fun101'),
    path('fun102/',views.fun102,name='fun102'),
    path('fun103/',views.fun103,name='fun103'),
]
