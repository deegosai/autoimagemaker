from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .models import Theme

# Create your views here.

@login_required(login_url='login')
def creth(request):
    return render(request, 'theme/create_theme.html', {'name': request.user})

# def edtth(request):
#     return render(request, 'theme/edit_theme.html')

# def manth(request):
#     theme = Theme.objects.all()
#     return render(request, 'theme/man_theme.html', {'thm': theme})
