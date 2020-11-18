from django.db import models

# Create your models here.

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    cat_img = models.ImageField('Category Thumb Image', upload_to='catthumb/')
    cat_name = models.CharField('Category', max_length=255, unique=True, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)