from django.urls import path
from .import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns =[ 
    path('frontblog/', views.frontblog, name= "frontblog"),
    path('<int:detail_id>', views.detail, name= "detail"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
]