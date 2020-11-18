from django.shortcuts import render

# Create your views here.

def pro(request):
    return render(request, 'adminprofile/profile.html')

def edtpro(request):
    return render(request, 'adminprofile/edit_pro.html')

def cpass(request):
    return render(request, 'adminprofile/change_pass.html')
