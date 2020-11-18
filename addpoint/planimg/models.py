from django.db import models

# from smartfields import fields
# from smartfields.dependencies import FileDependency
# from smartfields.processors import ImageProcessor

from subcriper.models import Subcriper
from subcription.models import Subcription
from client.models import Client

# Create your models here.


class Background(models.Model):
    sub_id = models.ForeignKey(Subcription, on_delete=models.CASCADE)
    background = models.ImageField(upload_to="background")
    x_logo = models.CharField('X_Angle_Logo', max_length=255, default="")
    y_logo = models.CharField('Y_Angle_Logo', max_length=255, default="")
    h_logo = models.CharField('Y_Hight_Logo', max_length=255, default="")
    x_txt = models.CharField('X_Angle_TXT', max_length=255, default="")
    y_txt = models.CharField('Y_Angle_TXT', max_length=255, default="")
    x_email = models.CharField('X_Angle_TXT', max_length=255,blank=True,default='')
    y_email = models.CharField('Y_Angle_TXT', max_length=255,blank=True,default='')
    x_contact = models.CharField('X_Angle_TXT', max_length=255,blank=True,default='')
    y_contact = models.CharField('Y_Angle_TXT', max_length=255,blank=True,default='')
    x_website = models.CharField('X_Angle_TXT', max_length=255,blank=True,default='')
    y_website = models.CharField('Y_Angle_TXT', max_length=255,blank=True,default='')
    font = models.CharField(max_length=50, default="")
    font_thickness = models.IntegerField(default=0)
    font_size = models.FloatField(default=0)
    font_color = models.CharField(max_length=50, default="")
    final_image = models.ImageField(upload_to="background/final", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Planimg(models.Model):
    pi_id = models.BigAutoField(primary_key=True)
    sbc_id = models.ForeignKey(Subcriper, on_delete=models.CASCADE)
    pi_img = models.ImageField('Plan Theme/Image', upload_to='planimage-theme/')
    cli_id = models.ForeignKey(Client, on_delete=models.CASCADE,null=True,blank=True)
    background_id = models.ForeignKey(Background ,on_delete=models.CASCADE,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)

