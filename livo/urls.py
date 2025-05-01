from django.urls import path
from rest_framework.response import Response
from .views import RoleListCreateView

from .views import SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup')
]