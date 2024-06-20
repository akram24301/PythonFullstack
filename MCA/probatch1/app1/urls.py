from django.urls import path
from . import views
urlpatterns=[
    path('displayhome/',views.displayhome,name='displayhome'),
    path('register/',views.register,name='register'),
    path('q18/',views.q18,name='q18'),
    path('fun1/',views.fun1,name='fun1'),
    path('fun2/',views.fun2,name='fun2'),
    path('fun3/',views.fun3,name='fun3'),
    

]
