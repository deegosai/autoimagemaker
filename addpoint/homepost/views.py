from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Homepost
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def addhp(request):
    if request.method == 'POST':
        hpimg = request.FILES['hpimg']
        sta = request.POST['sta']

        add = Homepost(hp_img=hpimg, status=sta)

        add.save()

        messages.success(request, 'Home Post Image Added Successfully', extra_tags='success')

        return HttpResponseRedirect('/hp/managehomepost/')

        # msg = {'serr':'Home Post Image Added Successfully'}
        # return render(request, 'homepost/add_post.html', {'err':msg, 'name': request.user})
    else:
        # msg = {'ferr':'Please Fill All Field Either Home Post Image Do Not Add.'}
        return render(request, 'homepost/add_post.html', {'name': request.user})

@login_required(login_url='login')
def edthp(request, eid):
    ehpo = Homepost.objects.get(pk=eid)
    return render(request, 'homepost/edit_post.html', {'ehp':ehpo, 'name': request.user})

@login_required(login_url='login')
def updhp(request, uhpid):
    if request.method == 'POST':
        try:
            if request.FILES['hpimg'] != 0:
                hpimg = request.FILES['hpimg']
                sta = request.POST['sta']

                edt = Homepost.objects.get(hp_id = uhpid)

                edt.hp_img = hpimg
                edt.status = sta

                edt.save()
        except:
            sta = request.POST['sta']

            edt = Homepost.objects.get(hp_id = uhpid)

            edt.hp_img = edt.hp_img
            edt.status = sta

            edt.save()

            messages.success(request, 'Home Post Image Updated Successfully', extra_tags='success')

            return HttpResponseRedirect('/hp/managehomepost/')

        messages.success(request, 'Home Post Image Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/hp/managehomepost/')

@login_required(login_url='login')
def delhp(request, did):
    de = Homepost.objects.get(pk=did)
    de.delete()
    messages.success(request, 'Home Post Image Deleted Successfully', extra_tags='danger')
    return HttpResponseRedirect('/hp/managehomepost/')

@login_required(login_url='login')
def manhp(request):
    hpo = Homepost.objects.all()
    return render(request, 'homepost/man_post.html', {'hp': hpo, 'name': request.user})