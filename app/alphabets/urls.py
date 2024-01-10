"""
URL mapping for the alphabets app
"""

from django.urls import path
from publish import views

urlpatterns = [
    path('', views.index, name='index')
]