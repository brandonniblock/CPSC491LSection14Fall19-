from django.contrib import admin
from .models import Upload

# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display = ('Meeting_Name', 'Meeting_Date', 
    'Meeting_Description', 'Meeting_Audio_File')
    
admin.site.register(Upload, UploadAdmin)
 