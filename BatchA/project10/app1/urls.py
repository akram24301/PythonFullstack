from django.urls import path
from . import views

urlpatterns=[
    path('display_teacher/',views.display_teacher,name='display_teacher'),
    ]