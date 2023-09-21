from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# class SampleClassView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "This is a protected class-based view."})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def sample_function_view(request):
#     return Response({"message": "This is a protected function-based view."})


class CustomTokenObtainPairView(TokenObtainPairView):
    # Personalizando el mensaje de respuesta
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['message'] = "Inicio de sesión exitoso."
        return response


class CustomTokenRefreshView(TokenRefreshView):
    # Personalizando el mensaje de respuesta
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['message'] = "Token JWT refrescado correctamente."
        return response
