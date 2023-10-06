"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog.admin import blog_site
from subscribe.admin import subscribe_site
from django.conf.urls.static import static
 

urlpatterns = [
    path('', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('blog_admin/', blog_site.urls),
    path('subscribe_admin/', subscribe_site.urls),
    path('', include('subscribe.urls')),
    path('summernote/', include('django_summernote.urls')),
    
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#if settings.DEBUG:
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




admin.site.index_title = "My Portfolio"
admin.site.site_header = "Horen Admin"
admin.site.site_title = "Horen Technologies"