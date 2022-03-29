from django.conf.urls import re_path
from django.contrib import admin

from EmployeeApp import views

urlpatterns = [
    re_path(r'^department$', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),
]