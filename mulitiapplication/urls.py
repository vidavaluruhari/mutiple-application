"""
URL configuration for mulitiapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from app2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_string/',app_string,name='app_string'),
    path('app_html/',app_html,name='app_html.html'),
    path('app2_string/',app2_string,name='app2_string'),
    path('app2_html/',app2_html,name='app2_html'),

]
