from django.contrib import admin
from app1.models import Ipaddress

class IpaddressAdmin(admin.ModelAdmin):
	list_display = ( 'ipaddress', 'status', 'description')


admin.site.register(Ipaddress)
