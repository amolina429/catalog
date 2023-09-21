from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CrearUsuarioView(CreateAPIView):
    permission_classes = [IsAuthenticated & IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
