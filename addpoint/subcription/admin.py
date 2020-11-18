from django.contrib import admin
from .models import Subcription

# Register your models here.

# @admin.register(Subcription)
# class SubcriptionAdmin(admin.ModelAdmin):
#     list_display=('sub_id', 'sub_name', 'sub_month', 'sub_price', 'final_price', 'sub_imgcount', 'created_date', 'updated_date', 'status')

admin.site.register(Subcription)
