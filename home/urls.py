"""
URL configuration for myToDO project.

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
from django.urls import path,include
from home import views

urlpatterns = [
  
    path('', views.login_page, name='login_page'),
    path('tasks', views.tasks, name='tasks'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('logout', views.logout_page, name='logout_page'),
    path('task_del/<id>', views.task_del, name='task_del'),
    path('task_upd/<id>', views.task_upd, name='task_upd'),
    path('task_upd/updated/<id>', views.updated, name='updated'),
    path('pending/<id>', views.pending, name='pending'),
    path('completed/<id>', views.completed, name='completed'),
]