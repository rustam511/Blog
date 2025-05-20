from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('main1/', views.main1, name='main1'),
]
