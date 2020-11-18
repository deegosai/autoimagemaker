from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Subcription
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def addsub(request):
    if request.method == 'POST':
        snm = request.POST['snm']
        mon = request.POST['mon']
        pr = request.POST['pr']
        # dis = request.POST['dis']
        fpr = request.POST['fpr']
        sta = request.POST['sta']
        if request.POST['tp'] is not None:
            tp = request.POST['tp']
            add = Subcription(sub_name=snm, sub_month=mon, sub_price=pr, final_price=fpr, status=sta)
        else:
            add = Subcription(sub_name=snm, sub_month=mon, sub_price=pr, final_price=fpr, sub_imgcount=tp, status=sta)
        add.save()

        messages.success(request, 'New Subcription Added Successfully', extra_tags='success')

        return HttpResponseRedirect('/sub/managesubcription/')

        # msg = {'serr':'New Subcription Added Successfully'}
        # return render(request, 'subcription/add_sub.html', {'err':msg, 'name': request.user})
    else:
        # msg = {'ferr':'Please Fill All Field Either New Subcription Do Not Add.'}
        return render(request, 'subcription/add_sub.html', {'name': request.user})

@login_required(login_url='login')
def edtsub(request, eid):
    sub = Subcription.objects.get(pk=eid)
    return render(request, 'subcription/edit_sub.html', {'sb':sub, 'name': request.user})

@login_required(login_url='login')
def updsub(request, usid):
    if request.method == 'POST':
        snm = request.POST['snm']
        mon = request.POST['mon']
        pr = request.POST['pr']
        fpr = request.POST['fpr']
        tp = request.POST['tp']
        sta = request.POST['sta']

        edt = Subcription.objects.get(sub_id = usid)

        edt.sub_name = snm
        edt.sub_month = mon
        edt.sub_price = pr
        edt.final_price = fpr
        edt.sub_imgcount = tp
        edt.status = sta
        edt.save()

        messages.success(request, 'Subcription Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/sub/managesubcription/')

@login_required(login_url='login')
def delsub(request, did):
    de = Subcription.objects.get(pk=did)
    de.delete()
    messages.success(request, 'Subcription Deleted Successfully', extra_tags='danger')
    return HttpResponseRedirect('/sub/managesubcription/')

@login_required(login_url='login')
def mansub(request):
    subcription = Subcription.objects.all()
    return render(request, 'subcription/man_sub.html', {'sub': subcription, 'name': request.user})
