from django.urls import path
from . import views

urlpatterns = [
    path('http/', views.http_response, name='http_response'),
    path('http_sub/', views.http_response_sub, name='http_response_sub'),
    path('json/', views.json_response, name='json_response'),
    path('stream/', views.streaming_response, name='streaming_response'),
    path('file/', views.file_response, name='file_response'),
]
