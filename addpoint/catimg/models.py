from django.db import models
from category.models import Category

# Create your models here.

class Catimg(models.Model):
    ci_id = models.BigAutoField(primary_key=True)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    ci_img = models.ImageField('Category Image', upload_to='catimg/')
    ci_blankimg = models.ImageField('Category Blank Image', upload_to='catblankimg/')
    x_logo = models.CharField('X_Angle_Logo', max_length=255, null=False)
    y_logo = models.CharField('Y_Angle_Logo', max_length=255, null=False)
    x_txt = models.CharField('X_Angle_TXT', max_length=255, null=False)
    y_txt = models.CharField('Y_Angle_TXT', max_length=255, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_TYPE_CHOICES = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)
