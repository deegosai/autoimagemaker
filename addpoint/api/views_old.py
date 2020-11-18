from django.shortcuts import render, redirect

from django.template import loader

import base64
from django.contrib.auth.hashers import make_password

from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Q

from django.core.mail import send_mail, EmailMultiAlternatives

from festivaltemp.settings import DOMAIN, PORT

import os

from category.models import Category
from catimg.models import Catimg
from client.models import Client
from clientgallery.models import Clientgallery
from homepost.models import Homepost
from subcriper.models import Subcriper
from subcription.models import Subcription

# Create your views here.

path='http://'+DOMAIN+':'+PORT+'/media/'

# Create your api views here.

# User Register Api
@api_view(['POST','GET'])
def u_register(request):
    if not (request.data['cli_fname'] and request.data['cli_lname'] and request.data['cli_mob'] and request.data['cli_email'] and request.data['cli_pass'] and request.FILES['com_img'] and request.data['com_name'] and request.data['com_email'] and request.data['com_mob'] and request.data['com_web'] and request.data['com_address']):

        return Response({'error_code': '5', 'error_string': "All Fields Can Not Be Empty.Please Fill All Mandatory Fields", 'data': "Null"})

    else:
        if Client.objects.filter(cli_email=request.data['cli_email']).exists():

            return Response({'error_code':'4','error_string':"User Email Is Already Exists. Try Another One",'data':"Null"})

        elif  Client.objects.filter(cli_mob=request.data['cli_mob']).exists():

            return Response({'error_code': '3', 'error_string': "User Mobile Number Already Is Exists. Try Another One", 'data': "Null"})

        elif Client.objects.filter(com_email=request.data['com_email']).exists():

            return Response({'error_code':'2','error_string':"Company Email Already Is Exists. Try Another One",'data':"Null"})

        elif  Client.objects.filter(com_mob=request.data['com_mob']).exists():

            return Response({'error_code': '1', 'error_string': "Company Mobile Number Is Already Exists. Try Another One", 'data': "Null"})

        elif  Client.objects.filter(com_web=request.data['com_web']).exists():

            return Response({'error_code': '6', 'error_string': "Company Domain Is Already Exists. Try Another One", 'data': "Null"})
            
        else:
            Client.objects.create(
                cli_fname=request.data['cli_fname'],
                cli_lname=request.data['cli_lname'],
                cli_mob=request.data['cli_mob'],
                cli_email=request.data['cli_email'],
                # cli_pass=make_password(request.data['cli_pass']),
                cli_pass=request.data['cli_pass'],
                com_img=request.FILES['com_img'],
                com_name=request.data['com_name'],
                com_email=request.data['com_email'],
                com_mob=request.data['com_mob'],
                com_web=request.data['com_web'],
                com_address=request.data['com_address'],
                status='Active'
            ) 

            userdata = Client.objects.values().last()

            return Response({'error_code':'0','error_string':"User Registration Successfully Done.",'data': userdata})

# User Login Api
@api_view(['POST','GET'])
def u_login(request):
    cli_email=request.POST['cli_email']
    cli_pass=request.POST['cli_pass']

    if not (cli_email and cli_pass):

        return Response({'error_code': '2', 'error_string': "User Email And Password Can Not Be Empty Or User Email And Password Are Mandatory", 'data': "Null"})

    else:
        if Client.objects.filter(cli_email=cli_email, cli_pass=cli_pass).exists():

            userdata = Client.objects.values().get(cli_email=cli_email,cli_pass=cli_pass)
            userdata['com_img']=path+userdata['com_img']

            return Response({'error_code':'0','error_string':"User Login Successfully",'data': userdata})

        else:
            
            return Response({'error_code': '1', 'error_string': "Wrong Email Or Password. Please Try Again.", 'data': 'Null'})

# Show Subscription Plan List Api
@api_view(['POST','GET'])
def sub(request):
    subscription = Subcription.objects.values().all()

    if subscription:

        return Response({'error_code': '0', 'error_string': "Show Subscription Plan List", 'data': subscription})

    else:

        return Response({'error_code': '1', 'error_string': "Subscription Data Not Found", 'data': "Null"})

# Show Home Post Api
@api_view(['POST','GET'])
def hp(request):
    homepost = Homepost.objects.values().all()
    for homepost1 in homepost:
        homepost1['hp_img'] = path+homepost1['hp_img']

    if homepost:

        return Response({'error_code': '0', 'error_string': "Show Home Post", 'data': homepost})

    else:

        return Response({'error_code': '1', 'error_string': "Home Post Data Not Found", 'data': "Null"})

# Show Category List Api
@api_view(['POST','GET'])
def cat(request):
    cat = Category.objects.values().all()
    for cat1 in cat:
        cat1['cat_img'] = path+cat1['cat_img']

    if cat:
    
        return Response({'error_code': '0', 'error_string': "Show Category List", 'data': cat})

    else:

        return Response({'error_code': '1', 'error_string': "Category Data Not Found", 'data': "Null"})

# User Profile Show Api
@api_view(['POST','GET'])
def usrpro(request):
    cli_id=request.POST['cli_id']

    if not (cli_id):

        return Response({'error_code': '2', 'error_string': "User Id Can Not Be Empty Or User Id Is Mandatory", 'data': "Null"})

    else:
        if Client.objects.filter(cli_id=cli_id).exists():

            pro = Client.objects.values().get(cli_id=cli_id)
            pro['com_img']=path+pro['com_img']

            return Response({'error_code':'0','error_string':"Show User Profile Details",'data': pro})

        else:
            
            return Response({'error_code': '1', 'error_string': "User Id Can Not Be Exists", 'data': 'Null'})

# Category Template Api
@api_view(['POST','GET'])
def catimg(request):
    ci = Catimg.objects.values().all()
    if ci:

        cat_id=request.POST['cat_id']

        if not (cat_id):

            return Response({'error_code': '2', 'error_string': "Category Id Can Not Be Empty Or Category Id Is Mandatory", 'data': "Null"})

        else:
            if Catimg.objects.filter(cat_id=cat_id).exists():

                catimg = Catimg.objects.values().filter(cat_id=cat_id).all()
                for catimg1 in catimg:
                    catimg1['ci_img']=path+catimg1['ci_img']
                    catimg1['ci_blankimg']=path+catimg1['ci_blankimg']

                return Response({'error_code':'0','error_string':"Show Category Template and Category Blank Template List",'data': catimg})

            else:
                
                return Response({'error_code': '1', 'error_string': "Category Id Can Not Be Exists", 'data': 'Null'})
    else:

        return Response({'error_code': '3', 'error_string': "Category Template Data Not Found", 'data': "Null"})

# User Profile Change Password Api
@api_view(['POST','GET'])
def cpass(request):
    cli_id=request.data['cli_id']
    cli_pass=request.data['cli_pass']

    if not (cli_id and cli_pass):

        return Response({'error_code': '2', 'error_string': "User Id And User Password Can Not Be Empty Or User Id And User Password Is Mandatory", 'data': "Null"})

    else:

        if Client.objects.filter(cli_id=cli_id).exists():

            Client.objects.filter(cli_id=cli_id).update(cli_pass=cli_pass)

            return Response({'error_code': '0', 'error_string': "User Password Changed Successfully", 'data': "Success"})

        else:    
            
            return Response({'error_code': '1', 'error_string': "User Id Can Not Be Exists", 'data': "Null"})

# Forgot Password Api
@api_view(['POST','GET'])
def fpass(request): 
    cli_email= request.data['cli_email']
    otp= request.data['otp']

    if not (cli_email and otp):

        return Response({'error_code': '2', 'error_string': "User Email And User OTP Can Not Be Empty Or User Email And User OTP Is Mandatory", 'data': "Null"})

    else:

        if Client.objects.filter(cli_email=cli_email).exists():

            send_mail(
            'OTP', 
            'Your otp is '+otp+'',
            'kishan@lucsoninfotech.com', 
            [cli_email, cli_email],     
            fail_silently=False,  
            )     

            fp = Client.objects.values().get(cli_email=cli_email)
            fp['com_img'] = path+fp['com_img']

            return Response({'error_code': '0', 'error_string': "OTP Has Been Sent To The Email. Please Check Your Email", 'data': fp})

        else: 

            return Response({'error_code': '1', 'error_string': "The Email You Enterd Is Invalid ", 'data': "Null"})

# User Update Profile Api
@api_view(['POST','GET'])
def updusr(request):
    cli_id=request.data['cli_id']

    if not (cli_id):

        return Response({'error_code': '2', 'error_string': "User Id Can Not Be Empty Or User Id Is Mandatory", 'data': "Null"})

    else:

        if Client.objects.filter(cli_id=cli_id).exists():

            try:

                if request.FILES['com_img'] != 0:

                    cli_fname = request.POST['cli_fname']
                    cli_lname = request.POST['cli_lname']
                    cli_mob = request.POST['cli_mob']
                    cli_email = request.POST['cli_email']
                    com_img = request.FILES['com_img']
                    com_name = request.POST['com_name']
                    com_email = request.POST['com_email']
                    com_mob = request.POST['com_mob']
                    com_web = request.POST['com_web']
                    com_address = request.POST['com_address']

                    edt = Client.objects.get(cli_id = cli_id)
                    edt.cli_fname = cli_fname
                    edt.cli_lname = cli_lname
                    edt.cli_mob = cli_mob
                    edt.cli_email = cli_email
                    edt.com_img = com_img
                    edt.com_name = com_name
                    edt.com_email = com_email
                    edt.com_mob = com_mob
                    edt.com_web = com_web
                    edt.com_address = com_address
                    
                    edt.save()

            except:

                cli_fname = request.POST['cli_fname']
                cli_lname = request.POST['cli_lname']
                cli_mob = request.POST['cli_mob']
                cli_email = request.POST['cli_email']
                com_name = request.POST['com_name']
                com_email = request.POST['com_email']
                com_mob = request.POST['com_mob']
                com_web = request.POST['com_web']
                com_address = request.POST['com_address']

                edt = Client.objects.get(cli_id = cli_id)
                edt.cli_fname = cli_fname
                edt.cli_lname = cli_lname
                edt.cli_mob = cli_mob
                edt.cli_email = cli_email
                edt.com_img = edt.com_img
                edt.com_name = com_name
                edt.com_email = com_email
                edt.com_mob = com_mob
                edt.com_web = com_web
                edt.com_address = com_address

                edt.save()

                return Response({'error_code': '0', 'error_string': "User Profile Updated Successfully", 'data': "Success"})

            return Response({'error_code': '0', 'error_string': "User Profile Updated Successfully", 'data': "Success"})

        else:    
            
            return Response({'error_code': '1', 'error_string': "User Id Can Not Be Exists", 'data': "Null"})

# User Active Plan Get Subscription Id Api
@api_view(['POST','GET'])
def subc(request):
    cli_id=request.POST['cli_id']

    if not (cli_id):

        return Response({'error_code': '2', 'error_string': "User Id Can Not Be Empty Or User Id Is Mandatory", 'data': "Null"})

    else:
        if Subcriper.objects.filter(cli_id=cli_id).exists():

            sid = Subcriper.objects.values().get(cli_id=cli_id)

            return Response({'error_code':'0','error_string':"Show User Subscription Plan Id",'data': sid})

        else:
            
            return Response({'error_code': '1', 'error_string': "User Id Can Not Be Exists", 'data': 'Null'})

# User Active Plan Api
@api_view(['POST','GET'])
def subscriber(request):
    sub_id=request.POST['sub_id']

    if not (sub_id):

        return Response({'error_code': '2', 'error_string': "User Subcription Id Can Not Be Empty Or User Subcription Id Is Mandatory", 'data': "Null"})

    else:
        if Subcription.objects.filter(sub_id=sub_id).exists():

            subc = Subcription.objects.values().get(sub_id=sub_id)

            return Response({'error_code':'0','error_string':"Show User Active Subscription Plan Details",'data': subc})

        else:
            
            return Response({'error_code': '1', 'error_string': "User Subcription Id Can Not Be Exists", 'data': 'Null'})

# Social Media Register Api
@api_view(['POST','GET'])
def sr(request):
    if not (request.data['token']):

        return Response({'error_code': '4', 'error_string':'User Token Can Not Be Empty Or User Token Is Mandatory', 'data': 'Null'})

    else: 

        mobile=Client.objects.filter(cli_mob=request.data['cli_mob']).count()

        email=Client.objects.filter(cli_email=request.data['cli_email']).count()

        token=Client.objects.filter(token=request.data['token']).count()

        if mobile==1:

                userdata = Client.objects.values().get(cli_mob=request.data['cli_mob'])

                return Response({'error_code': '3', 'error_string': "User Mobile Number Already Exists", 'data': userdata})

        elif email==1:

                userdata = Client.objects.values().get(cli_email=request.data['cli_email'])

                return Response({'error_code': '2', 'error_string': "User Email Already Exists",'data': userdata})

        elif token==1:

                userdata = Client.objects.values().get(token=request.data['token'])

                return Response({'error_code': '1', 'error_string': "User Token Already Exists",'data': userdata})

        else: 

                Client.objects.create(
                    cli_fname = request.data['cli_fname'],
                    cli_mob=request.data['cli_mob'],
                    cli_email=request.data['cli_email'],
                    type=request.data['type'],
                    token=request.data['token']
                )

                userdata = Client.objects.values().last()

                return Response({'error_code': '0', 'error_string': "User Registration Successfully Done.", 'data': userdata})

# Social Media Login Api
@api_view(['POST','GET'])
def sl(request):
    cli_mob=request.data['cli_mob'] 
    cli_email=request.data['cli_email']  
    token=request.data['token'] 

    if cli_mob!="":  

        if Client.objects.filter(cli_mob=cli_mob).exists():

            userdata = Client.objects.values().get(cli_mob=cli_mob)
            userdata['com_img'] = path+userdata['com_img'] 
   
            return Response({'error_code': '0', 'error_string': "User Login Successfully", 'data': userdata})

        else:

            return Response({'error_code': '1', 'error_string': "You Have Entered Incorrect Details", 'data': 'Null'})

    if cli_email!="":

        if Client.objects.filter(cli_email=cli_email).exists():

            userdata = Client.objects.values().get(cli_email=cli_email)
            userdata['com_img'] = path+userdata['com_img']

            return Response({'error_code': '0', 'error_string': "User Login Successfully", 'data': userdata})

        else:

            return Response({'error_code': '1', 'error_string': "You Have Entered Incorrect Details", 'data': 'Null'})

    if token!="":    

        if Client.objects.filter(token=token).exists():  

            userdata = Client.objects.values().get(token=token)
            userdata['com_img'] = path+userdata['com_img']

            return Response({'error_code': '0', 'error_string': "User Login Successfully", 'data': userdata})

        else: 

            return Response({'error_code': '1', 'error_string': "You Have Entered Incorrect Details", 'data': 'Null'})

# Register Otp Api
@api_view(['POST','GET'])
def otp(request):
    cli_email= request.data['cli_email']
    otp= request.data['otp']

    if not (cli_email and otp):

        return Response({'error_code': '1', 'error_string': "User Email And User OTP Can Not Be Empty Or User Email And User OTP Is Mandatory", 'data': "Null"})

    else:

        send_mail(
        'OTP', 
        'Your otp is '+otp+'',
        'kishan@lucsoninfotech.com', 
        [cli_email, cli_email],     
        fail_silently=False,  
        )

        return Response({'error_code': '0', 'error_string': "User Registration OTP Has Been Sent To The Email. Please Check Your Email", 'data': 'Success'})