from django.urls import path
from rest_framework.response import Response
from .views import RoleListCreateView


urlpatterns = [
    path('roles/', RoleListCreateView.as_view(), name='role-list-create')
]