from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def addcat(request):
    if request.method == 'POST':

        cimg = request.FILES['cimg']
        cnm = request.POST['cnm']
        sta = request.POST['sta']

        add = Category(cat_img=cimg, cat_name=cnm, status=sta)
        add.save()

        messages.success(request, 'Category Added Successfully', extra_tags='success')

        return HttpResponseRedirect('/cat/managecategory/')

        # msg = {'serr':'Category Added Successfully'}
        # return render(request, 'category/add_cat.html', {'err':msg, 'name': request.user})
    else:
        # msg = {'ferr':'Please Fill All Field Either Category Do Not Add.'}
        return render(request, 'category/add_cat.html', {'name': request.user})

@login_required(login_url='login')
def edtcat(request, eid):
    ecat = Category.objects.get(pk=eid)
    return render(request, 'category/edit_cat.html', {'ect':ecat, 'name': request.user})

@login_required(login_url='login')
def updcat(request, ucid):
    if request.method == 'POST':
        try:
            if request.FILES['cimg'] != 0:
                cimg = request.FILES['cimg']
                cnm = request.POST['cnm']
                sta = request.POST['sta']

                edt = Category.objects.get(cat_id = ucid)

                edt.cat_img = cimg
                edt.cat_name = cnm
                edt.status = sta
                edt.save()
        except:
            cnm = request.POST['cnm']
            sta = request.POST['sta']

            edt = Category.objects.get(cat_id = ucid)

            edt.cat_img = edt.cat_img
            edt.cat_name = cnm
            edt.status = sta
            edt.save()

            messages.success(request, 'Category Updated Successfully', extra_tags='success')

            return HttpResponseRedirect('/cat/managecategory/')

        messages.success(request, 'Category Updated Successfully', extra_tags='success')

        return HttpResponseRedirect('/cat/managecategory/')

@login_required(login_url='login')
def delcat(request, did):
    de = Category.objects.get(pk=did)
    de.delete()

    messages.error(request, 'Category Deleted Successfully', extra_tags='danger')

    return HttpResponseRedirect('/cat/managecategory/')

@login_required(login_url='login')
def mancat(request):
    category = Category.objects.all()
    return render(request, 'category/man_cat.html', {'cat': category, 'name': request.user})
