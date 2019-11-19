"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib.auth.views import LogoutView


import jobs.views
import management.views as manage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),        
    path('viewers/', jobs.views.viewers, name='viewers'),
    path('blog/', include('blog.urls')),
    path('manage/', manage_views.manage, name='manage'),
    path('', include('social_django.urls', namespace='social')),
    path('ckeditor/', include('ckeditor_uploader.urls') ),
    path(
        'logout/',
        LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL),
        name='logout'
        ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
