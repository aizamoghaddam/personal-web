from django.urls import path
from .views import *


urlpatterns = [
    path('', work, name='work')
]

