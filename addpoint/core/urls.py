from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminlogin, name='login'),
    path('dashboard/', views.dashboard, name='dash'),
    path('logout/', views.adminlogout, name='logout'),

    path('adminprofile/', views.pro, name='pro'),
    path('adminchangepassword/', views.cpass, name='cpass'),

    path('editadminprofile/<str:eid>/', views.edt, name='edt'),
    path('updateadminprofile/<int:uid>/', views.upd, name='upd'),

    # path('deleteadminprofile/<str:did>/', views.del, name='del'),
]