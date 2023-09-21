from django.urls import path
from .views import CreateRollView

urlpatterns = [
    path('users/rol/create/', CreateRollView.as_view(), name='create_rol'),
]
