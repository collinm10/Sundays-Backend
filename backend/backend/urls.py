"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers
from sundays import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('week-assignments/', views.get_assignments ),
    path('user-classes/', views.get_classes),
    path('create-class/', views.create_class),
    path('create-class/', views.create_class),
    path('set-completed/', views.set_completed),
    path('update-due-date/', views.update_due_date),
    path('get-asses-class/', views.get_ass_types_class),
    path('log-me-in/', views.log_me_in),
    path('sign-me-up/', views.sign_me_up),
    path('update-assignment/', views.update_assignment)
]
