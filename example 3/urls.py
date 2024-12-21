from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_message, name='submit_message'),
    path('get/', views.get_messages, name='get_messages'),
]
