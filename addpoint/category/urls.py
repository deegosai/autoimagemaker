from django.urls import path
from . import views

urlpatterns = [

    # Add, Update, Delete, Edit Data Urls
    path('addcategory/', views.addcat, name='addcat'),
    path('editcategory/<str:eid>/', views.edtcat, name='edtcat'),
    path('updatecategory/<int:ucid>/', views.updcat, name='updcat'),
    path('deletecategory/<str:did>/', views.delcat, name='delcat'),

    # Fetch Or Other Data Urls
    path('managecategory/', views.mancat, name='mancat'),
    
]