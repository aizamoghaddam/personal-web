from django.urls import path
from .views import *

urlpatterns = [
    path('', about, name='about')
]