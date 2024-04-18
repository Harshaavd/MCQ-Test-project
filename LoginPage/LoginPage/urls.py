"""
URL configuration for LoginPage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/',views.Lg_page, name='login'),
    path('',views.home, name='home'),
    path('reg/',views.reg_page, name='register'),
    path('logout/',views.logout_page, name='logout'),
    path('que2/',views.q2_list, name='questions2'),
    path('que3/',views.q3_list, name='questions3'),
    path('que4/',views.q4_list, name='questions4'),
    path('addque/',views.que_page, name='addquestion'),
    path('addque2/',views.que2_page, name='addquestion2'),
    path('addque3/',views.que3_page, name='addquestion3'),
    path('addque4/',views.que4_page, name='addquestion4'),
]
