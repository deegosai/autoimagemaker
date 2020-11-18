from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addsubcription/', views.addsub, name='addsub'),
    path('editsubcription/<str:eid>/', views.edtsub, name='edtsub'),
    path('updatesubcription/<int:usid>/', views.updsub, name='updsub'),
    path('deletesubcription/<str:did>/', views.delsub, name='delsub'),

    # Fetch Or Other Data Urls
    path('managesubcription/', views.mansub, name='mansub'),

]