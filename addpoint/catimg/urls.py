from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addcategoryimage/', views.addci, name='addci'),
    path('editcategoryimage/<str:eid>/', views.edtci, name='edtci'),
    path('updatecategoryimage/<int:uciid>/', views.updci, name='updci'),
    path('deletecategoryimage/<str:did>/', views.delci, name='delci'),

    # Fetch Or Other Data Urls
    path('managecategoryimage/', views.manci, name='manci'),
    
]