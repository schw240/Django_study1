from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('Country/', views.CountryView),
    path('Customer/', views.CustomerView),
    path('Customer/<pk>', views.CustomerDetailView),
]