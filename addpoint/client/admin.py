from django.contrib import admin
from .models import Client

# Register your models here.

# @admin.register(ModelClassName, site=custom_admin_site)


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display=('cli_id', 'cli_fname', 'cli_lname', 'cli_mob', 'cli_email', 'cli_pass', 'com_img', 'com_name', 'com_email', 'com_mob', 'com_web', 'com_address', 'created_date', 'updated_date', 'status')
    
    
admin.site.register(Client)
