from django.urls import path
from .views import CrearUsuarioView

urlpatterns = [
    path('create/', CrearUsuarioView.as_view(), name='create_user'),
]
