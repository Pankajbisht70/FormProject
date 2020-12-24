from django.contrib import admin
from .models import *


# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','married','city']


class AcademicAdmin(admin.ModelAdmin):
    list_display = ['course', 'passing_year']
    course = models.CharField(max_length=30)
    passing_year = models.IntegerField


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_role','Years']
    company_name = models.CharField(max_length=30)
    job_role = models.CharField(max_length=30)
    Years = models.IntegerField


admin.site.register(Personal_info,PersonalAdmin)
admin.site.register(Academic_info,AcademicAdmin)
admin.site.register(Experience_info,ExperienceAdmin)

