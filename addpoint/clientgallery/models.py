from django.db import models
from client.models import Client

# Create your models here.

class Clientgallery(models.Model):
    clig_id = models.BigAutoField(primary_key=True)
    cli_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    clig_img = models.ImageField('Client Gallery', upload_to='clientgallery/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)
