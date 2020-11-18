from django.shortcuts import render, HttpResponseRedirect ,redirect
from django.contrib import messages
from .models import Planimg,Background
from subcription.models import Subcription
from client.models import Client
from subcriper.models import Subcriper,Client
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import cv2
import os
import numpy as np
from datetime import datetime
from PIL import Image,ImageGrab
from django.templatetags.static import static
# Create your views here.

@login_required(login_url='login')
def addpi(request):
    subc = Subcription.objects.all()
    if request.method == 'POST': 
                # pbimg = request.FILES['planimg']
                # xlg = request.POST['position_logo_x']
                # ylg = request.POST['position_logo_y']
                # hlg = request.POST['logo_height']
                # xtxt = request.POST['position_address_x']
                # ytxt = request.POST['position_address_y']
                # xemail = request.POST['position_email_x']
                # yemail = request.POST['position_email_y']
                # xcontact = request.POST['position_contact_x']
                # ycontact = request.POST['position_contact_y']
                # xwebsite = request.POST['position_website_x']
                # ywebsite = request.POST['position_website_y']
                # choose_supscriper = request.POST['choose_supscriper']
                if 'planimg' in request.FILES:
                    pbimg = request.FILES['planimg']
                    background = createImages(request)
                # subcriper = Subcriper.objects.get(sbc_id=choose_supscriper)
                # add = Planimg(  sbc_id=subcriper, 
                #                 pi_img=pbimg, 
                #                 x_logo=xlg, 
                #                 y_logo=ylg, 
                #                 h_logo=hlg,
                #                 x_txt=xtxt, 
                #                 y_txt=ytxt,
                #                 x_email=xemail,
                #                 y_email=yemail,
                #                 x_contact=xcontact,
                #                 y_contact=ycontact,
                #                 x_website=xwebsite,
                #                 y_website=ywebsite,
                #                 status="Active"
                #                 )
                # add.save()
                # preview_images = Background.objects.all()
                return render(request,"planimg/preview.html" , {'background':background})
                # return HttpResponseRedirect('/pimg/manageplanimage/')
           
    return render(request, 'planimg/add_planning_image.html', {'subc':subc, 'name': request.user})

@login_required(login_url='login')
def updateplanimage(request,subscriber_id):
    if request.method == 'POST':
        background = Background.objects.get(id=subscriber_id)
        background.x_logo = x = request.POST['position_logo_x']
        background.y_logo = y = request.POST['position_logo_y']
        background.h_logo = height = request.POST['logo_height']
        background.x_txt = xtxt = request.POST['position_address_x']
        background.y_txt = ytxt = request.POST['position_address_y']
        background.x_email = xemail = request.POST['position_email_x']
        background.y_email = yemail = request.POST['position_email_y']
        background.x_contact = xcontact = request.POST['position_contact_x']
        background.y_contact = ycontact = request.POST['position_contact_y']
        background.x_website = xwebsite = request.POST['position_website_x']
        background.y_website = ywebsite = request.POST['position_website_y']
        background.font = choose_font = request.POST['choose_font']
        background.font_thickness = choose_font_thickness = int(request.POST['choose_font_thickness'])
        background.font_size = choose_font_size = float(request.POST['choose_font_size'])
        background.font_color = favcolor = request.POST['favcolor']
        if 'planimg' in request.FILES:
            pbimg = request.FILES['planimg']
        background = updateImages(request)

        return render(request,"planimg/preview.html" , {'background':background})
    return render(request,"planimg/man_planimg.html")

@login_required(login_url='login')
def edtpi(request, eid):
    epi = Planimg.objects.get(pk=eid)
    subc = Subcriper.objects.all()
    return render(request, 'planimg/edit_planning_image.html', {'epi':epi, 'subc':subc, 'name': request.user})

@login_required(login_url='login')
def editpreview(request, eid):
    background = Background.objects.get(pk=eid)
    subcribers = Subcription.objects.all()
    return render(request, 'planimg/edit_planning_image.html', {'background':background, 'subcribers':subcribers })

@login_required(login_url='login')
def updpi(request, upiid):
    if request.method == 'POST':
            pid = upiid
            xlg = request.POST['position_logo_x']
            ylg = request.POST['position_logo_y']
            hlg = request.POST['logo_height']
            xtxt = request.POST['position_address_x']
            ytxt = request.POST['position_address_y']
            xemail = request.POST['position_email_x']
            yemail = request.POST['position_email_y']
            xcontact = request.POST['position_contact_x']
            ycontact = request.POST['position_contact_y']
            xwebsite = request.POST['position_website_x']
            ywebsite = request.POST['position_website_y']

            if 'planimg' in request.FILES:
                ptimg = request.FILES['planimg']
                createImages(request)
                
            edt = Planimg.objects.get(pi_id = upiid)

            if 'planimg' in request.FILES:
                edt.pi_img = ptimg
            edt.x_logo = xlg
            edt.y_logo = ylg
            edt.x_txt = xtxt
            edt.y_txt = ytxt

            edt.x_email = xemail
            edt.y_email = yemail
            edt.x_contact = xcontact
            edt.y_contact = ycontact
            edt.x_website = xwebsite
            edt.y_website = ywebsite
            edt.save()

    return HttpResponseRedirect('/pimg/manageplanimage/')

@login_required(login_url='login')
def delpi(request, did):
    de = Background.objects.get(pk=did)
    de.delete()
    messages.success(request, 'Plan Image/Theme Deleted Successfully', extra_tags='danger')
    return HttpResponseRedirect('/pimg/manageplanimage/')

@login_required(login_url='login')
def manpi(request):
    pi = Background.objects.all()
    return render(request, 'planimg/man_planimg.html', {'pi': pi})


@login_required(login_url='login')
def generateimages(request,did):
    pi = Planimg.objects.all()
    background = Background.objects.get(id=did)
    createFinalImages(request,background)
    return redirect("manpi")

@login_required(login_url='login')
def planusers(request, bgid):
    pi = Planimg.objects.filter(background_id=bgid)
    return render(request, 'planimg/user_plan_list.html', {'pi': pi, 'name': request.user})

# FUNCTION FOR IMAGE GENERATE 
def createImages(request):
    pbimg = request.FILES['planimg']
    sub_id = Subcription.objects.get(sub_id = request.POST['choose_supscriper'])
    background = Background.objects.create(sub_id = sub_id,background = pbimg)
    background.x_logo = x = request.POST['position_logo_x']
    background.y_logo = y = request.POST['position_logo_y']
    background.h_logo = height = request.POST['logo_height']
    background.x_txt = xtxt = request.POST['position_address_x']
    background.y_txt = ytxt = request.POST['position_address_y']
    background.x_email = xemail = request.POST['position_email_x']
    background.y_email = yemail = request.POST['position_email_y']
    background.x_contact = xcontact = request.POST['position_contact_x']
    background.y_contact = ycontact = request.POST['position_contact_y']
    background.x_website = xwebsite = request.POST['position_website_x']
    background.y_website = ywebsite = request.POST['position_website_y']
    background.font = choose_font = request.POST['choose_font']
    background.font_thickness = choose_font_thickness = int(request.POST['choose_font_thickness'])
    background.font_size = choose_font_size = float(request.POST['choose_font_size'])
    background.font_color = favcolor = request.POST['favcolor']

    favcolor = favcolor.lstrip('#')
    favcolor = tuple(int(favcolor[i:i+2], 16) for i in (0, 2, 4))
    favcolor = (favcolor[2],favcolor[1],favcolor[0])
    overlay = static('/images/logo3.png')
    bg = cv2.imread(background.background.url[1:], -1)
    ol = cv2.imread(overlay[1:], -1)

    o_h, o_w, o_ch = ol.shape
    imgScale = int(height)/o_w
    new_o_h,new_o_w = int(o_h*imgScale), int(o_w*imgScale)
    ol = cv2.resize(ol,(new_o_w, new_o_h))
    
    result_1 = overlay_transparent(bg, ol, int(x), int(y))

    if choose_font == "FONT_HERSHEY_SIMPLEX" : choose_font = cv2.FONT_HERSHEY_SIMPLEX
    if choose_font == "FONT_HERSHEY_PLAIN" : choose_font = cv2.FONT_HERSHEY_PLAIN
    if choose_font == "FONT_HERSHEY_DUPLEX" : choose_font = cv2.FONT_HERSHEY_DUPLEX
    if choose_font == "FONT_HERSHEY_COMPLEX" : choose_font = cv2.FONT_HERSHEY_COMPLEX
    if choose_font == "FONT_HERSHEY_TRIPLEX" : choose_font = cv2.FONT_HERSHEY_TRIPLEX
    if choose_font == "FONT_HERSHEY_COMPLEX_SMALL" : choose_font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if choose_font == "FONT_HERSHEY_SCRIPT_SIMPLEX" : choose_font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    if choose_font == "FONT_HERSHEY_SCRIPT_COMPLEX" : choose_font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

    result_1 = cv2.putText(result_1, "Company Name", (int(xtxt),int(ytxt)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    result_1 = cv2.putText(result_1, "example@gmail.com", (int(xemail),int(yemail)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    result_1 = cv2.putText(result_1, "+91 9876543210", (int(xcontact),int(ycontact)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    result_1 = cv2.putText(result_1, "example.com", (int(xwebsite),int(ywebsite)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    path = os.getcwd() 
    path = path + '/media/Images'
    img_name = path + "/merged-"+str(datetime.now()).replace(":","")+".png"
    cv2.imwrite(img_name, result_1)
    img_name.replace(path,'')
    background.final_image = img_name[26:]
    background.save()
    return background

def updateImages(request):
    background = Background.objects.get(id = request.POST['id'])
    if 'planimg' in request.FILES:
        background = Background.objects.get(id = request.POST['id'])
        background.background = request.FILES['planimg']
        background.save()

    background.sub_id = Subcription.objects.get(sub_id = request.POST['choose_supscriper'])
    background.x_logo = x = request.POST['position_logo_x']
    background.y_logo = y = request.POST['position_logo_y']
    background.h_logo = height = request.POST['logo_height']
    background.x_txt = xtxt = request.POST['position_address_x']
    background.y_txt = ytxt = request.POST['position_address_y']
    background.x_email = xemail = request.POST['position_email_x']
    background.y_email = yemail = request.POST['position_email_y']
    background.x_contact = xcontact = request.POST['position_contact_x']
    background.y_contact = ycontact = request.POST['position_contact_y']
    background.x_website = xwebsite = request.POST['position_website_x']
    background.y_website = ywebsite = request.POST['position_website_y']
    background.font = choose_font = request.POST['choose_font']
    background.font_thickness = choose_font_thickness = int(request.POST['choose_font_thickness'])
    background.font_size = choose_font_size = float(request.POST['choose_font_size'])
    background.font_color = favcolor = request.POST['favcolor']

    favcolor = favcolor.lstrip('#')
    favcolor = tuple(int(favcolor[i:i+2], 16) for i in (0, 2, 4))
    favcolor = (favcolor[2],favcolor[1],favcolor[0])
    overlay = static('/images/logo3.png')
    bg = cv2.imread(background.background.url[1:], -1)
    ol = cv2.imread(overlay[1:], -1)

    o_h, o_w, o_ch = ol.shape
    imgScale = int(height)/o_w
    new_o_h,new_o_w = int(o_h*imgScale), int(o_w*imgScale)
    ol = cv2.resize(ol,(new_o_w, new_o_h))
    
    result_1 = overlay_transparent(bg, ol, int(x), int(y))

    if choose_font == "FONT_HERSHEY_SIMPLEX" : choose_font = cv2.FONT_HERSHEY_SIMPLEX
    if choose_font == "FONT_HERSHEY_PLAIN" : choose_font = cv2.FONT_HERSHEY_PLAIN
    if choose_font == "FONT_HERSHEY_DUPLEX" : choose_font = cv2.FONT_HERSHEY_DUPLEX
    if choose_font == "FONT_HERSHEY_COMPLEX" : choose_font = cv2.FONT_HERSHEY_COMPLEX
    if choose_font == "FONT_HERSHEY_TRIPLEX" : choose_font = cv2.FONT_HERSHEY_TRIPLEX
    if choose_font == "FONT_HERSHEY_COMPLEX_SMALL" : choose_font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if choose_font == "FONT_HERSHEY_SCRIPT_SIMPLEX" : choose_font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    if choose_font == "FONT_HERSHEY_SCRIPT_COMPLEX" : choose_font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

    result_1 = cv2.putText(result_1, "Company Name", (int(xtxt),int(ytxt)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    result_1 = cv2.putText(result_1, "example@gmail.com", (int(xemail),int(yemail)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    result_1 = cv2.putText(result_1, "+91 9876543210", (int(xcontact),int(ycontact)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    result_1 = cv2.putText(result_1, "example.com", (int(xwebsite),int(ywebsite)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
    # img_name = "/merged-"+str(datetime.now()).replace(":","")+".png"
    # cv2.imwrite(img_name, result_1)
    path = os.getcwd() 
    path = path + '/media/Images'
    img_name = path + "/merged-"+str(datetime.now()).replace(":","")+".png"
    cv2.imwrite(img_name, result_1)
    img_name.replace(path,'')
    background.final_image = img_name[26:] 
    # background.final_image = img_name
    background.save()
    return background

# Generate Total Images For Plan 

def createFinalImages(request,background):

    sbcid = Subcription.objects.get(sub_id = background.sub_id.sub_id)
    # if sbcid.sub_imgcount > sbcid.sub_remain_imgcount:
    x = background.x_logo
    y = background.y_logo
    height = background.h_logo
    xtxt = background.x_txt
    ytxt = background.y_txt
    xemail = background.x_email
    yemail = background.y_email
    xcontact = background.x_contact 
    ycontact = background.y_contact
    xwebsite = background.x_website
    ywebsite = background.y_website
    choose_font = background.font
    choose_font_thickness = background.font_thickness
    choose_font_size = background.font_size
    favcolor = background.font_color

    favcolor = favcolor.lstrip('#')
    favcolor = tuple(int(favcolor[i:i+2], 16) for i in (0, 2, 4))
    favcolor = (favcolor[2],favcolor[1],favcolor[0])
    accounts = Subcriper.objects.filter(sub_id=background.sub_id.sub_id)
    for account in accounts:
        if account.image_count == None or int(account.image_count) > 0:
            new_sbc_id = account.sbc_id
            my_acount = Subcriper.objects.get(sub_id=account.sub_id.sub_id,cli_id=account.cli_id.cli_id,sbc_id=new_sbc_id)
            if account.image_count != None and my_acount.sub_id.sub_id != 1:
                my_acount.image_count = int(my_acount.image_count) - 1
                my_acount.save()
            account = Client.objects.get(cli_id=account.cli_id.cli_id)
            overlay = account.com_img.url    # ad point logo
            bg = cv2.imread(background.background.url[1:], -1)
            ol = cv2.imread(overlay[1:], -1)

            o_h, o_w, o_ch = ol.shape
            imgScale = int(height)/o_w
            new_o_h,new_o_w = int(o_h*imgScale), int(o_w*imgScale)
            ol = cv2.resize(ol,(new_o_w, new_o_h))
            
            result_1 = overlay_transparent(bg, ol, int(x), int(y))

            if choose_font == "FONT_HERSHEY_SIMPLEX" : choose_font = cv2.FONT_HERSHEY_SIMPLEX
            if choose_font == "FONT_HERSHEY_PLAIN" : choose_font = cv2.FONT_HERSHEY_PLAIN
            if choose_font == "FONT_HERSHEY_DUPLEX" : choose_font = cv2.FONT_HERSHEY_DUPLEX
            if choose_font == "FONT_HERSHEY_COMPLEX" : choose_font = cv2.FONT_HERSHEY_COMPLEX
            if choose_font == "FONT_HERSHEY_TRIPLEX" : choose_font = cv2.FONT_HERSHEY_TRIPLEX
            if choose_font == "FONT_HERSHEY_COMPLEX_SMALL" : choose_font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            if choose_font == "FONT_HERSHEY_SCRIPT_SIMPLEX" : choose_font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
            if choose_font == "FONT_HERSHEY_SCRIPT_COMPLEX" : choose_font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

            result_1 = cv2.putText(result_1, account.com_name, (int(xtxt),int(ytxt)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
            result_1 = cv2.putText(result_1, account.com_email, (int(xemail),int(yemail)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
            result_1 = cv2.putText(result_1, account.com_mob, (int(xcontact),int(ycontact)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
            result_1 = cv2.putText(result_1, account.com_web, (int(xwebsite),int(ywebsite)), choose_font, choose_font_size, favcolor, choose_font_thickness, cv2.LINE_AA, False) 
            path = os.getcwd() 
            path = path + '/media/Images'
            img_name = path + "/merged-"+str(datetime.now()).replace(":","")+".png"
            cv2.imwrite(img_name, result_1)
            img_name.replace(path,'')
            sub_id = Subcriper.objects.get(sub_id=background.sub_id.sub_id,cli_id=account.cli_id,sbc_id=new_sbc_id)
            planimg = Planimg()
            planimg.sbc_id = sub_id
            planimg.pi_img = img_name[26:]
            planimg.background_id=background
            account = Client.objects.get(cli_id=account.cli_id)
            planimg.cli_id = account
            planimg.save()

    messages.success(request, 'Plan Image/Images of This plan is created successfully')


def overlay_transparent(background, overlay, x, y):

    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background