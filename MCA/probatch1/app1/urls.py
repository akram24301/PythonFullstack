from django.urls import path
from . import views
urlpatterns=[
    path('displayhome/',views.displayhome,name='displayhome'),
    path('displayq1/',views.displayq1,name='displayq1'),
    path('displayq2/',views.displayq2,name='displayq2'),
    path('displayq3/',views.displayq3,name='displayq3'),
    path('displayq4/',views.displayq4,name='displayq4'),
    path('frameq9/',views.frameq9,name='frameq9'),
    path('displaygreen/',views.displaygreen,name='displaygreen'),
    path('register/',views.register,name='register'),
    path('q18/',views.q18,name='q18'),
    path('fun1/',views.fun1,name='fun1'),
    path('fun2/',views.fun2,name='fun2'),
    path('fun3/',views.fun3,name='fun3'), 

]
