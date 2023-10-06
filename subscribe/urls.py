from django.urls import path
from .import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns =[
    path('subscribe/', views.subscribe, name='subscribe'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('static/img/favicon.ico'))),
]