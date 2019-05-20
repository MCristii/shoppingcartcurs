from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'orders'

urlpatterns = [
    path('order/', views.order, name='order')
]