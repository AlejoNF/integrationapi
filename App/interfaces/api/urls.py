# App/interfaces/api/urls.py
from django.urls import path
from .helloController import HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello-world'),
]