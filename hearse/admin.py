from django.contrib import admin
from .models import Request, Hearse
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = "driver_name","email",'color','model','driver_phone','Price','location','hearse_image'

admin.site.register(Hearse, MemberAdmin)

# requests
class MemberAdmin(admin.ModelAdmin):
    list_display = "fullname","From",'To','email','Day','time'

admin.site.register(Request, MemberAdmin)
