from django.db import models

# Create your models here.

class Subcription(models.Model):
    sub_id = models.BigAutoField(primary_key=True)
    sub_name = models.CharField("Subcription Name", max_length=255)
    sub_month = models.IntegerField('Month Of Plan', null=False)
    sub_price = models.IntegerField('Subcription Price')
    # discount = models.CharField('Discount Of Plan Price', max_length=255)
    final_price = models.IntegerField('final Price', null=False)
    sub_imgcount = models.IntegerField('Subcription Provide Theme',null=True,default=None)
    sub_remain_imgcount = models.IntegerField('Subcription Remain Theme',blank=True,null=True,default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    ) 
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)