"""emi_web URL Configuration

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
#from django.contrib import admin
#from django.urls import path ,include
#
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('polls/', include ("polls.urls")),
#    url(r'^site/(?P<path>.*)$', serve,
#        {'document_root': SITE_ROOT, 'show_indexes': True},
#        name='site_path'
#    ]
####
import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic.base import TemplateView

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('users/', include('users.urls')),
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
        'show_indexes'  : True}, name='site_path'),
    path('', TemplateView.as_view(template_name='home/main.html')),
    path("hello/", include("hello.urls")),
    path('accounts/', include('django.contrib.auth.urls')),  #
    path('autos/', include('autos.urls')),                   #
    # path('authz/', include('authz.urls')),
    path("cats/", include("cats.urls")),
]


