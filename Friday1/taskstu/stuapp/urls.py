from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name="home"),
    path('create_view/',views.create_view,name="create_view"),
    path('list_view/',views.list_view,name="list_view"),
    path('<id>/', views.detail_view ,name='detail_view'),
    path('<id>/update_view/', views.update_view ,name='update_view'),
    path('<id>/delete_view/',views.delete_view ,name='delete_view' ),
]