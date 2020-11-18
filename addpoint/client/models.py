from django.db import models
# Create your models here.

class Client(models.Model):
    cli_id = models.BigAutoField(primary_key=True)
    cli_fname = models.CharField('First Name', max_length=255,blank=True,null=True,default=None)
    cli_lname = models.CharField('Last Name', max_length=255,blank=True,null=True,default=None)
    cli_mob = models.CharField('Mobile', max_length=20, unique=True, null=True, blank=True,default=None)
    cli_email = models.EmailField('Email', unique=True, null=True, blank=True,default=None)
    cli_pass = models.CharField('Password', max_length=255, null=True ,blank=True,default=None)
    com_img = models.ImageField('Company Logo', upload_to='companylogo/')
    com_name = models.CharField('Company Name', max_length=255, null=False)
    com_email = models.EmailField('Email', null=True,default=None)
    com_mob = models.CharField('Mobile', max_length=20, null=True,default=None)
    com_web = models.CharField('Company Website', max_length=255, unique=True, null=True)
    com_address = models.TextField('Company Address')
    token = models.CharField('Social Token', max_length=255)
    type = models.CharField('Social Type', max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)

    # def __str__(self):
    #     return self.cli_fname

    # def __str__(self):
    #     return str(self.cli_id)
    
