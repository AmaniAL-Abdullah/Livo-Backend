from django.urls import path
from rest_framework.response import Response

from .views import (
    RoleListCreateView,
    SignUpView, 
    RoleDetailView,
    RoleTasksView,
    TaskListCreateView,
    TaskDetailView)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),

    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('roles/<int:pk>/tasks/', RoleTasksView.as_view(), name='role_tasks'),
    path('task/<int:pk>/',TaskDetailView.as_view(), name='task_detail'),
]