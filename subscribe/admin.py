from django.contrib import admin
from .models import Subscribe
from .import models

# Register your models here.
class SubscribeAdminArea(admin.AdminSite):
    site_header = 'Subscribe Amdin Area'
    
subscribe_site = SubscribeAdminArea(name='SubscribeAdmin')

subscribe_site.register(models.Subscribe)
