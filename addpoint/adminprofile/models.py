from django.db import models

# Create your models here.

class Adminprofile(models.Model):
    aid = models.BigAutoField(primary_key=True)
    img = models.ImageField('Admin Image', upload_to='adminpro/')
    fname = models.CharField('Admin First Name', max_length=255)
    lname = models.CharField('Admin Last Name', max_length=255)
    oc = models.TextField('Admin Organization Or Company Name')
    mobile = models.CharField('Admin Mobile', unique=True, max_length=12, null=False)
    email = models.EmailField('Admin Email', unique=True, max_length=254, null=False)
    password = models.CharField('Admin Password', max_length=255, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)
