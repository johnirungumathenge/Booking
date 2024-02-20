from django.contrib import admin
from .models import User
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = "fullname","email",'phone','password'

admin.site.register(User, MemberAdmin)