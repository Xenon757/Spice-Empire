from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.menuScreen),
    path("companies", views.displayAllCompanies),
]
