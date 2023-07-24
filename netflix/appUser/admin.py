from django.contrib import admin
from appUser.models import *

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display=('user','name','loginp','id')
    

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    
    list_display=('user','subscribe','id')