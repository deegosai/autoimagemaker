from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Clientgallery
from client.models import Client
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def addclig(request):
    cli = Client.objects.all()
    if request.method == 'POST':
        cliid = request.POST['cliid']
        cligimg = request.FILES.getlist('cligimg')
        sta = request.POST['sta']
        for cligimg1 in cligimg:
            add = Clientgallery(cli_id_id=cliid, clig_img=cligimg1, status=sta)
            
            add.save()

        messages.success(request, 'Client Gallery Image Added Successfully', extra_tags='success')

        return HttpResponseRedirect('/cligly/manageclientgallery/')
        
        # msg = {'serr':'Client Gallery Image Added Successfully'}
        # return render(request, 'clientgallery/add_clig.html', {'err':msg, 'cli':cli, 'name': request.user})
    else:
        # msg = {'ferr':'Please Fill All Field Either Client Gallery Image Do Not Add.'}
        return render(request, 'clientgallery/add_clig.html', {'cli':cli, 'name': request.user})
    return render(request, 'clientgallery/add_clig.html', {'cat':cat, 'name': request.user})

@login_required(login_url='login')
def edtclig(request, eid):
    eclig = Clientgallery.objects.get(pk=eid)
    cli = Client.objects.all()
    return render(request, 'clientgallery/edit_clig.html', {'eclig':eclig, 'cli':cli, 'name': request.user})

@login_required(login_url='login')
def updclig(request, ucligid):
    if request.method == 'POST':
        try:
            if request.FILES['cligimg'] != 0:
                cliid = request.POST['cliid']
                cligimg = request.FILES['cligimg']
                sta = request.POST['sta']

                edt = Clientgallery.objects.get(clig_id = ucligid)

                edt.cli_id_id = cliid
                edt.clig_img = cligimg
                edt.status = sta

                edt.save()
        except:
            cliid = request.POST['cliid']
            sta = request.POST['sta']

            edt = Clientgallery.objects.get(clig_id = ucligid)

            edt.cli_id_id = cliid
            edt.clig_img = edt.clig_img
            edt.status = sta

            edt.save()

            messages.success(request, 'Client Gallery Image Updated Successfully', extra_tags='success')

            return HttpResponseRedirect('/cligly/manageclientgallery/')

        messages.success(request, 'Client Gallery Image Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/cligly/manageclientgallery/')

@login_required(login_url='login')
def delclig(request, did):
    de = Clientgallery.objects.get(pk=did)
    de.delete()
    messages.success(request, 'Client Gallery Image Deleted Successfully', extra_tags='danger')
    return HttpResponseRedirect('/cligly/manageclientgallery/')

@login_required(login_url='login')
def manclig(request):
    clig = Clientgallery.objects.all()
    return render(request, 'clientgallery/man_clig.html', {'clig': clig, 'name': request.user})