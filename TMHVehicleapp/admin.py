from django.contrib import admin
from .models import profile,vehicle_master,booking,role_master
# Register your models here.

admin.site.register(profile)
admin.site.register(vehicle_master)
admin.site.register(booking)
admin.site.register(role_master)
