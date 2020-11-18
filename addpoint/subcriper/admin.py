from django.contrib import admin
from .models import Subcriper

# Register your models here.

# @admin.register(Subcriper)
# class SubcriperAdmin(admin.ModelAdmin):
#     list_display=('sbc_id', 'uid', 'sub_id', 'created_date', 'updated_date', 'status')

admin.site.register(Subcriper)