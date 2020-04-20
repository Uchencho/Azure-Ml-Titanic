from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('predict/', views.predicter, name='predict'),
]