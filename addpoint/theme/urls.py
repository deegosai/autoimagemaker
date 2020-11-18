from django.urls import path
from . import views

urlpatterns = [
    path('createtheme/', views.creth, name='creth'),
    # path('edittheme/', views.edtth, name='edtth'),
    # path('managetheme/', views.manth, name='manth'),
]