from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world_template, name='hello_world_html'),
]
