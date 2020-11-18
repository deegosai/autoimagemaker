from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Catimg
from category.models import Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def addci(request):
    cat = Category.objects.all()
    if request.method == 'POST':
        cid = request.POST['cid']
        cimg = request.FILES['cimg']
        cbimg = request.FILES['cbimg']
        xlg = request.POST['xlg']
        ylg = request.POST['ylg']
        xtxt = request.POST['xtxt']
        ytxt = request.POST['ytxt']
        sta = request.POST['sta']

        add = Catimg(cat_id_id=cid, ci_img=cimg, ci_blankimg=cbimg, x_logo=xlg, y_logo=ylg, x_txt=xtxt, y_txt=ytxt, status=sta)

        add.save()

        messages.success(request, 'Category Image Added Successfully', extra_tags='success')

        return HttpResponseRedirect('/ci/managecategoryimage/')

        # msg = {'serr':'Category Image Added Successfully'}
        # return render(request, 'catimg/add_catimg.html', {'err':msg, 'cat':cat, 'name': request.user})
    else:
        # msg = {'ferr':'Please Fill All Field Either Category Image Do Not Add.'}
        return render(request, 'catimg/add_catimg.html', {'cat':cat, 'name': request.user})
    return render(request, 'catimg/add_catimg.html', {'cat':cat, 'name': request.user})

@login_required(login_url='login')
def edtci(request, eid):
    ecati = Catimg.objects.get(pk=eid)
    cat = Category.objects.all()
    return render(request, 'catimg/edit_catimg.html', {'eci':ecati, 'cat':cat, 'name': request.user})

@login_required(login_url='login')
def updci(request, uciid):
    if request.method == 'POST':
        try:
            if request.FILES['cimg'] != 0 and request.FILES['cbimg'] != 0:
                cid = request.POST['cid']
                cimg = request.FILES['cimg']
                cbimg = request.FILES['cbimg']
                xlg = request.POST['xlg']
                ylg = request.POST['ylg']
                xtxt = request.POST['xtxt']
                ytxt = request.POST['ytxt']
                sta = request.POST['sta']

                edt = Catimg.objects.get(ci_id = uciid)

                edt.cat_id_id = cid
                edt.ci_img = cimg
                edt.ci_blankimg = cbimg
                edt.x_logo = xlg
                edt.y_logo = ylg
                edt.x_txt = xtxt
                edt.y_txt = ytxt
                edt.status = sta

                edt.save()
        except:
            cid = request.POST['cid']
            xlg = request.POST['xlg']
            ylg = request.POST['ylg']
            xtxt = request.POST['xtxt']
            ytxt = request.POST['ytxt']
            sta = request.POST['sta']

            edt = Catimg.objects.get(ci_id = uciid)

            edt.cat_id_id = cid
            edt.ci_img = edt.ci_img
            edt.ci_blankimg = edt.ci_blankimg
            edt.x_logo = xlg
            edt.y_logo = ylg
            edt.x_txt = xtxt
            edt.y_txt = ytxt
            edt.status = sta

            edt.save()

            messages.success(request, 'Category Image Updated Successfully', extra_tags='success')

            return HttpResponseRedirect('/ci/managecategoryimage/')

        messages.success(request, 'Category Image Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/ci/managecategoryimage/')

@login_required(login_url='login')
def delci(request, did):
    de = Catimg.objects.get(pk=did)
    de.delete()
    messages.success(request, 'Category Image Deleted Successfully', extra_tags='danger')
    return HttpResponseRedirect('/ci/managecategoryimage/')

@login_required(login_url='login')
def manci(request):
    cati = Catimg.objects.all()
    return render(request, 'catimg/man_catimg.html', {'ci': cati, 'name': request.user})