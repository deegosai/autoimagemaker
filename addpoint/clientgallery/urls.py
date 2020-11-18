from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addclientgallery/', views.addclig, name='addclig'),
    path('editclientgallery/<str:eid>/', views.edtclig, name='edtclig'),
    path('updateclientgallery/<int:ucligid>/', views.updclig, name='updclig'),
    path('deleteclientgallery/<str:did>/', views.delclig, name='delclig'),

    # Fetch Or Other Data Urls
    path('manageclientgallery/', views.manclig, name='manclig'),
    
]