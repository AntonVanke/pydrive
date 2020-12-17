# App url 配置
from django.urls import path

from App import views

urlpatterns = [
    path('', views.index)
]
