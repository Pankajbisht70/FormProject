from django.contrib import admin
from FormApp.models import IndiaJobs
# Register your models here.

class Indiajobsadmin(admin.ModelAdmin):
    list_display = ['Name','Education','City','Position']


admin.site.register(IndiaJobs,Indiajobsadmin)
