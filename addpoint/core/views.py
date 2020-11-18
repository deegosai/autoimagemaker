from django.shortcuts import render, HttpResponseRedirect
# from .forms import EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from client.models import Client
from category.models import Category
from catimg.models import Catimg
from subcriper.models import Subcriper

# Create your views here.

def adminlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Admin Logged In Successfully', extra_tags='success')
                    return HttpResponseRedirect('/dashboard/')
        else: 
            fm = AuthenticationForm()
        return render(request, 'core/adminlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

# def dashboard(request):
#     if request.user.is_authenticated:
#         return render(request, 'core/dashboard.html', {'name': request.user})
#     else:
#         return HttpResponseRedirect('/')

#     return render(request, 'core/dashboard.html')

def dashboard(request):
    cli = Client.objects.all().count()
    cat = Category.objects.all().count()
    cati = Catimg.objects.all().count()
    subc = Subcriper.objects.all().count()

    if request.user.is_authenticated:
        return render(request, 'core/dashboard.html', {'name': request.user, 'cli':cli, 'cat':cat, 'cati':cati, 'subc':subc})
    else:
        return HttpResponseRedirect('/')

    return render(request, 'core/dashboard.html')

# Logout
def adminlogout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='login')
def pro(request):
    # admin = User.objects.all()
    return render(request, 'core/profile.html', {'name': request.user, 'fnm': request.user.first_name, 'lnm': request.user.last_name, 'em': request.user.email, 'id': request.user.id})

# @login_required(login_url='login')
# def upd(request):
#     return render(request, 'core/edit_pro.html', {'name': request.user,})
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             if request.user.is_superuser == True:
#                 fm = EditUserProfileForm(request.POST, instance=request.user)
#                 users = User.objects.all()
#             else:
#                 fm = EditUserProfileForm(request.POST, instance=request.user)
#                 users = None
#         if fm.is_valid():
#             messages.success(request, 'Admin Profile Updated Successfully !!!')
#             fm.save()
#         else:
#         if request.user.is_superuser == True:
#             fm = EditUserProfileForm(instance=request.user)
#             users = User.objects.all()
#         else:
#             fm = EditUserProfileForm(instance=request.user)
#             users = None
#         return render(request, 'core/edit_pro.html', {'name': request.user.username, 'form':fm, 'users':users})
#     else:
#         return HttpResponseRedirect('/')

@login_required(login_url='login')
def edt(request, eid):
    eusr = User.objects.get(id=eid)
    usr = User.objects.all()
    return render(request, 'core/edit_pro.html', {'eusr':eusr, 'usr':usr, 'name': request.user})

@login_required(login_url='login')
def upd(request, uid):
    if request.method == 'POST':
        unm = request.POST['unm']
        fnm = request.POST['fnm']
        lnm = request.POST['lnm']
        em = request.POST['em']

        edt = User.objects.get(id = uid)
        edt.username = unm
        edt.first_name = fnm
        edt.last_name = lnm
        edt.email = em

        edt.save()

        messages.success(request, 'Admin Profile Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/adminprofile/')

# @login_required(login_url='login')
# def cpass(request):
#     return render(request, 'core/change_pass.html', {'name': request.user})

# Change Password with old Password
def cpass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Admin Password Changed Successfully', extra_tags='success')
                return HttpResponseRedirect('/adminprofile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'core/change_pass.html', {'form':fm, 'name': request.user})
    else:
        return HttpResponseRedirect('/')

# Signup View Function
# def sign_up(request):
#  if request.method == "POST":
#   fm = SignUpForm(request.POST)
#   if fm.is_valid():
#    messages.success(request, 'Account Created Successfully !!') 
#    fm.save()
#  else: 
#   fm = SignUpForm()
#  return render(request, 'enroll/signup.html', {'form':fm})

# Login View Function
# def user_login(request):
#   if not request.user.is_authenticated:
#     if request.method == "POST":
#       fm = AuthenticationForm(request=request, data=request.POST)
#       if fm.is_valid():
#         uname = fm.cleaned_data['username']
#         upass = fm.cleaned_data['password']
#         user = authenticate(username=uname, password=upass)
#         if user is not None:
#           login(request, user)
#           messages.success(request, 'Logged in successfully !!')
#           return HttpResponseRedirect('/profile/')
#     else: 
#       fm = AuthenticationForm()
#     return render(request, 'enroll/userlogin.html', {'form':fm})
#   else:
#     return HttpResponseRedirect('/profile/')

# Profile
# def user_profile(request):
#   if request.user.is_authenticated:
#     return render(request, 'enroll/profile.html', {'name': request.user})
#   else:
#     return HttpResponseRedirect('/login/')



