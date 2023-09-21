from django.urls import path
from .views import CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'token', CustomTokenObtainPairView, 'token_obtain_pair')
# router.register(r'token/refresh', CustomTokenRefreshView, 'token_refresh')

urlpatterns = [
    # path('class-view/', SampleClassView.as_view(), name='class-view'),
    # path('function-view/', sample_function_view, name='function-view'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
