from django.contrib import admin
from .import models
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Amdin Area'
    
blog_site = BlogAdminArea(name='BlogAdmin')



class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    
# admin.site.register(models.post_blog, SummerAdmin)
# admin.site.register(models.post_blog, SummerAdmin)
blog_site.register(models.post_blog, SummerAdmin)