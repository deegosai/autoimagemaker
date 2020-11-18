from django.db import models
from client.models import Client
from subcription.models import Subcription

# Create your models here.

class Subcriper(models.Model):
    sbc_id = models.BigAutoField(primary_key=True)
    cli_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subcription, on_delete=models.CASCADE)
    start_date = models.CharField('Plan Start Date', max_length=255, null=True,default=None)
    end_date = models.CharField('Plan End Date', max_length=255, null=True,default=None)
    image_count = models.IntegerField('Total Image Remaining',default=None,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)
