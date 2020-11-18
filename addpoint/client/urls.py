from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addclient/', views.addcli, name='addcli'),
    path('editclient/<str:eid>/', views.edtcli, name='edtcli'),
    path('updateclient/<int:ucliid>/', views.updcli, name='updcli'),
    path('deleteclient/<str:did>/', views.delcli, name='delcli'),

    # Fetch Or Other Data Urls
    path('manageclient/', views.mancli, name='mancli'),
    # path('clientgallery/<str:glyid>/', views.clig, name='cligly'),
    # path('subcription/<int:subid>/', views.sub, name='sub'),
    
]