"""Formproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from FormApp import views as v1
from SessionApp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.welcome),
    path('Index/', v1.welcome),
    path('AddForm/', v1.add_form),
    path('Listjob/', v1.view_job),
    path('Personal/', v2.personal_view),
    path('Academic/', v2.academic_view),
    path('Experience/', v2.experience_view),
    path('Display/', v2.display),

    ]