from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home ,name='name'),
    path('<int:id>',show , name='show'),
]