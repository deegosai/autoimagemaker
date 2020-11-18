from django.urls import path
from . import views

urlpatterns = [
    path('adminprofile/', views.pro, name='pro'),
    path('editprofile/', views.edtpro, name='edtpro'),
    path('changepassword/', views.cpass, name='cpass'),
]