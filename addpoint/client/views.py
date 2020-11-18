from django.shortcuts import render, HttpResponseRedirect
import base64
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Client
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from subcriper.models import Subcriper
from clientgallery.models import Clientgallery

# Create your views here.

@login_required(login_url='login')
def addcli(request):
    if request.method == 'POST':
        if request.POST['pas'] == request.POST['cpas']:
            fnm = request.POST['fnm']
            lnm = request.POST['lnm']
            mob = request.POST['mob']
            em = request.POST['em'].lower()
            pas = request.POST['pas']
            # cpas = request.post['cpas']

            cimg = request.FILES['cimg']
            cnm = request.POST['cnm']
            cem = request.POST['cem'].lower()
            cmob = request.POST['cmob']
            cweb = request.POST['cweb']
            cadd = request.POST['cadd']

            sta = request.POST['sta']
            add = Client(cli_fname=fnm, cli_lname=lnm, cli_mob=mob, cli_email=em, cli_pass=pas, com_img=cimg, com_name=cnm, com_email=cem, com_mob=cmob, com_web=cweb, com_address=cadd, status=sta)
            
            add.save()
        else:
            messages.success(request, 'Client Password And Confirm Password Do Not Match. Please Try Again!', extra_tags='danger')

            return render(request, 'client/add_cli.html', {'name': request.user})


        messages.success(request, 'Client Added Successfully', extra_tags='success')

        return HttpResponseRedirect('/cli/manageclient/')
        
        # msg = {'serr':'Client Added Successfully'}
        # return render(request, 'client/add_cli.html', {'err':msg, 'name': request.user})
    else:
        # msg = {'ferr':'Please Fill All Field Either Client Do Not Add.'}
        return render(request, 'client/add_cli.html', {'name': request.user})

@login_required(login_url='login')
def edtcli(request, eid):
    ecli = Client.objects.get(pk=eid)
    cli = Client.objects.all()
    return render(request, 'client/edit_cli.html', {'ecli':ecli, 'cli':cli, 'name': request.user})

@login_required(login_url='login')
def updcli(request, ucliid):
    if request.method == 'POST':
        try:
            if request.FILES['cimg'] != 0:
                fnm = request.POST['fnm']
                lnm = request.POST['lnm']
                mob = request.POST['mob']
                em = request.POST['em'].lower()
                cimg = request.FILES['cimg']
                cnm = request.POST['cnm']
                cem = request.POST['cem'].lower()
                cmob = request.POST['cmob']
                cweb = request.POST['cweb']
                cadd = request.POST['cadd']
                sta = request.POST['sta']

                edt = Client.objects.get(cli_id = ucliid)
                edt.cli_fname = fnm
                edt.cli_lname = lnm
                edt.cli_mob = mob
                edt.cli_email = em
                edt.com_img = cimg
                edt.com_name = cnm
                edt.com_email = cem
                edt.com_mob = cmob
                edt.com_web = cweb
                edt.com_address = cadd
                edt.status = sta

                edt.save()
        except:
            fnm = request.POST['fnm']
            lnm = request.POST['lnm']
            mob = request.POST['mob']
            em = request.POST['em'].lower()
            cnm = request.POST['cnm']
            cem = request.POST['cem'].lower()
            cmob = request.POST['cmob']
            cweb = request.POST['cweb']
            cadd = request.POST['cadd']
            sta = request.POST['sta']

            edt = Client.objects.get(cli_id = ucliid)
            edt.cli_fname = fnm
            edt.cli_lname = lnm
            edt.cli_mob = mob
            edt.cli_email = em
            edt.com_img = edt.com_img
            edt.com_name = cnm
            edt.com_email = cem
            edt.com_mob = cmob
            edt.com_web = cweb
            edt.com_address = cadd
            edt.status = sta

            edt.save()

            messages.success(request, 'Client Updated Successfully', extra_tags='success')

            return HttpResponseRedirect('/cli/manageclient/')

        messages.success(request, 'Client Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/cli/manageclient/')

@login_required(login_url='login')
def delcli(request, did):
    de = Client.objects.get(pk=did)
    de.delete()
    messages.success(request, 'Client Deleted Successfully', extra_tags='danger')
    return HttpResponseRedirect('/cli/manageclient/')

@login_required(login_url='login')
def mancli(request):
    cli = Client.objects.filter().reverse()
    cli = reversed(list(cli))
    return render(request, 'client/man_cli.html', {'cli': cli, 'name': request.user})

# @login_required(login_url='login')
# def sub(request, subid):
#     try:
#         sub = Subcriper.objects.get(cli_id = subid)
#         return render(request, 'client/subcription.html', {'sub': sub, 'name': request.user})
#     except:
#         sub1 = 'Sorry, No Any Subscription Plan Active'
#         return render(request, 'client/subcription.html', {'sub1': sub1, 'name': request.user})

# @login_required(login_url='login')
# def clig(request, glyid):
#     try:
#         clig = Clientgallery.objects.filter(cli_id = glyid)
#         return render(request, 'client/cli_gallery.html', {'clig': clig, 'name': request.user})
#     except:
#         return render(request, 'client/cli_gallery.html', {'name': request.user})