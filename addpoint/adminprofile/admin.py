from django.contrib import admin
from .models import Adminprofile

admin.site.register (Adminprofile)

# @admin.register(Adminprofile)
# class AdminprofileAdmin(admin.ModelAdmin):
#     list_display=('aid', 'img', 'fname', 'lname', 'oc', 'mobile', 'email', 'password', 'created_date', 'updated_date', 'status')

# admin.site.register(Adminprofile)