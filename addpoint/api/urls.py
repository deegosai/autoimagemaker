from django.urls import path
from . import views

urlpatterns = [

# FOR USER LOGIN
    # Api Urls
    path('user_register/', views.u_register, name='reg'),
    path('user_login/', views.u_login, name='log'),
    path('subscription_plan/', views.sub, name='sub'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    # path('homepost/', views.hp, name='hp'),
    # path('category/', views.cat, name='cat'),

# FOR USER PLAN 
    path('user_active_plan/', views.subc, name='uaplan'),
    path('user_plan_date/', views.dt, name='update'),
    path('user_plan_image/', views.pi, name='pi'),
    path('homepost/', views.hp, name='hp'),

# FOR USER UPDATE OR FORGATE
    path('user_profile/', views.usrpro, name='usrpro'),
    # path('category_template/', views.catimg, name='catimg'),
    path('user_change_password/', views.cpass, name='cpass'),
    path('forgot_password/', views.fpass, name='fpass'),
    path('update_user_profile/', views.updusr, name='updusr'),

# FOR SOCIAL LOGIN
    # path('subscriber/', views.subscriber, name='subscriber'),
    path('socialmedia_register/', views.sr, name='sr'),
    path('socialmedia_login/', views.sl, name='sl'),
    path('user_register_otp/', views.otp, name='otp'),

]