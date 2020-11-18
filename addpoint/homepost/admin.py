from django.contrib import admin
from .models import Homepost

# Register your models here.

# @admin.register(Homepost)
# class HomepostAdmin(admin.ModelAdmin):
#     list_display=('hp_id', 'hp_img', 'created_date', 'updated_date', 'status')

admin.site.register(Homepost)