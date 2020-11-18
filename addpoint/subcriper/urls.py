from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addsubcriper/', views.addspr, name='addspr'),
    path('editsubcriper/<str:eid>/', views.edtspr, name='edtspr'),
    path('updatesubcriper/<int:usprid>/', views.updspr, name='updspr'),
    path('deletesubcriper/<str:did>/', views.delspr, name='delspr'),
    path('getCount/<str:id>/', views.getCount, name='getCount'),

    # Fetch Or Other Data Urls
    path('managesubcriper/', views.manspr, name='manspr'),
    
]