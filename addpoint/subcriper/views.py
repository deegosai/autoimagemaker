from django.shortcuts import render, HttpResponseRedirect , HttpResponse
from django.contrib import messages
from .models import Subcriper
from client.models import Client
from subcription.models import Subcription
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import pandas as pd
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
# Create your views here.

@login_required(login_url='login')
def addspr(request):
    cli = Client.objects.filter(status="Active")
    sub = Subcription.objects.all()
    if request.method == 'POST':
        if request.FILES['client_list'] is None:
            cliid = request.POST['cliid']
            subid = request.POST['subid']

            # sd = request.POST['sd']
            # ed = request.POST['ed']
            # sta = request.POST['sta']
            sub = Subcription.objects.get(sub_id=subid)
            count = sub.sub_imgcount

            # add = Subcriper(cli_id_id=cliid, sub_id_id=subid, start_date=sd, end_date=ed, status=sta,image_count=count)
            add = Subcriper(cli_id_id=cliid, sub_id_id=subid,image_count=count)

            add.save()

            messages.success(request, 'Subcriper Added Successfully', extra_tags='success')

            return HttpResponseRedirect('/spr/managesubcriper/')
        else:
            print(request.FILES['client_list'])
            excel_file = request.FILES['client_list']
            movies_sheet1 = pd.read_excel(excel_file)
            print(movies_sheet1.head(11))

            for i in range(len(movies_sheet1.count())):
                wb = load_workbook(request.FILES['client_list'])
                sheet = wb['plan']
                print(sheet)
                image_loader = SheetImageLoader(sheet)
                if i != 0 and i != 1:
                    ePath = "E" + str(i)
                    image = image_loader.get(ePath)
                    image.thumbnail

        # msg = {'serr':'Subcriper Added Successfully'}
        # return render(request, 'subcriper/add_subc.html', {'err':msg, 'cli':cli, 'sub':sub, 'name': request.user})
    else:
        # msg = {'ferr':'Please Fill All Field Either Subcriper Do Not Add.'}
        return render(request, 'subcriper/add_subc.html', {'cli':cli, 'sub':sub, 'name': request.user})
    return render(request, 'subcriper/add_subc.html', {'usr':usr, 'sub':sub, 'name': request.user})

@login_required(login_url='login')
def edtspr(request, eid):
    esp = Subcriper.objects.get(pk=eid)
    cli = Client.objects.all()
    sub = Subcription.objects.all()
    return render(request, 'subcriper/edit_subc.html', {'espr':esp, 'cli':cli, 'sub':sub, 'name': request.user})

@login_required(login_url='login')
def updspr(request, usprid):
    if request.method == 'POST':
        cliid = request.POST['cliid']
        subid = request.POST['subid']
        sd = request.POST['sd']
        ed = request.POST['ed']
        sta = request.POST['sta']
        count = request.POST['count']

        edt = Subcriper.objects.get(sbc_id = usprid)

        edt.cli_id_id = cliid
        edt.sub_id_id = subid
        edt.start_date = sd
        edt.end_date = ed
        edt.status = sta
        edt.image_count = count

        edt.save()

        messages.success(request, 'Subcriper Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/spr/managesubcriper/')

@login_required(login_url='login')
def delspr(request, did):
    de = Subcriper.objects.get(pk=did)
    de.delete()
    messages.success(request, 'Subcriper Deleted Successfully', extra_tags='danger')
    return HttpResponseRedirect('/spr/managesubcriper/')

@login_required(login_url='login')
def manspr(request):
    sp = Subcriper.objects.filter()
    return render(request, 'subcriper/man_subc.html', {'spr': sp, 'name': request.user})

@login_required(login_url='login')
def getCount(request,id):
    subcription = Subcription.objects.get(sub_id=request.POST['id'])
    count = subcription.sub_imgcount
    return HttpResponse({'count':count})