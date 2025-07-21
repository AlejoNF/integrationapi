# App/interfaces/api/urls.py
from django.urls import path
from .helloController import HelloWorldView
from .empaqueController import EmpaqueView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello-world'),
    path('empaques/', EmpaqueView.as_view(), name='empaque-create'),           # POST para crear
    path('empaques/<int:pk>/', EmpaqueView.as_view(), name='empaque-update'),  # PUT para actualizar
]