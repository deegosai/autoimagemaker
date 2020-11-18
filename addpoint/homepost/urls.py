from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addhomepost/', views.addhp, name='addhp'),
    path('edithomepost/<str:eid>/', views.edthp, name='edthp'),
    path('updatehomepost/<int:uhpid>/', views.updhp, name='updhp'),
    path('deletehomepost/<str:did>/', views.delhp, name='delhp'),

    # Fetch Or Other Data Urls
    path('managehomepost/', views.manhp, name='manhp'),
    
]