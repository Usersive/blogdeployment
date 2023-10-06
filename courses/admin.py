from django.contrib import admin
from .models import Courses
from .models import Service
from .import models
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Courses)



class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    
admin.site.register(models.Courses, SummerAdmin)
admin.site.register(models.Service, SummerAdmin)