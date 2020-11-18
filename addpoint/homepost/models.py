from django.db import models

# Create your models here.

class Homepost(models.Model):
    hp_id = models.BigAutoField(primary_key=True)
    hp_img = models.ImageField('Home Post Image', upload_to='homepost/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)
