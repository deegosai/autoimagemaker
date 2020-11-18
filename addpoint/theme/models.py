from django.db import models
# from category.models import Category

# Create your models here.

# class Theme(models.Model):
#     tid = models.BigAutoField(primary_key=True)
#     cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     image = models.ImageField('Theme', upload_to='theme/', null=False)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#     STATUS_TYPE_CHOICES = (
#         ('Active', 'Active'),
#         ('Deactive', 'Deactive'),
#     )
#     status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=10)