from django.contrib import admin
from.models import *

class Projectadmin(admin.ModelAdmin):
    list_display = ['id','project_name','text','translated_to_language','created_at','updated_at']

admin.site.register(Project,Projectadmin)

class Orderadmin(admin.ModelAdmin):
    list_display = ['id','project_id','status','translated_tex','created_at','updated_at']
admin.site.register(Order,Orderadmin)


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','latname','email','username','date_of_birth','mobile_number']