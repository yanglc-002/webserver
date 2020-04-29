from django.contrib import admin
from cmdb import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.group)
admin.site.register(models.host_idc)
admin.site.register(models.host_manager)
admin.site.register(models.host_list)



