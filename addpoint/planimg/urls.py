from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addplanimage/', views.addpi, name='addpi'),
    path('editplanimage/<str:eid>/', views.edtpi, name='edtpi'),
    path('editpreview/<str:eid>/', views.editpreview, name='editpreview'),
    path('updateplanimage/<int:subscriber_id>/', views.updateplanimage, name='updateplanimage'),
    path('updateplanimage/<int:upiid>/', views.updpi, name='updpi'),
    path('deleteplanimage/<str:did>/', views.delpi, name='delpi'),
    path('generateimages/<str:did>/', views.generateimages, name='generateimages'),

    # Fetch Or Other Data Urls
    path('manageplanimage/', views.manpi, name='manpi'),
    path('planusers/<str:bgid>/', views.planusers, name='planusers'),
    
]