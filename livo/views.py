from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Role, Task, Achievement
from .serializers import RoleSerializers, TaskSerializers, AchievementSerializers

from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


# Create your views here.

# Model Role
class RoleListCreateView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        role = Role.objects.filter(owner=request.user)
        serializer = RoleSerializers(role, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = RoleSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
#.....................................................
class RoleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user): 
        role = get_object_or_404(Role, pk=pk)
        if role.owner != user:
            raise PermissionDenied(" You do not have permission to access this role.")
        return role

    def get(self, request, pk):
        role = self.get_object(pk, request.user)
        serializer = RoleSerializers(role)
        return Response(serializer.data, status=200)
    
    def delete(self, request, pk):
        role = self.get_object(pk, request.user)
        role.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        role = self.get_object(pk, request.user)
        serializer = RoleSerializers(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
#---------------------------------------------------------

# Model Task

# Returns all tasks for a specific role owned by the authenticated user
class RoleTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        role = get_object_or_404(Role, pk=pk, owner=request.user)
        tasks = role.task.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data, status=200)

# Handles creating a new task and listing all tasks for the authenticated user
class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        task = Task.objects.filter(role__owner=request.user)
        serializer = TaskSerializers(task, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = TaskSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
# Returns details of a single task if it belongs to the authenticated user
class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user): 
        task = get_object_or_404(Task, pk=pk)
        if task.role.owner != user:
            raise PermissionDenied(" You do not have permission to access this Task.")
        return task

    def get(self, request, pk):
        task = self.get_object(pk, request.user)
        serializer = TaskSerializers(task)
        return Response(serializer.data, status=200)
    
    def patch(self, request, pk):
        task = self.get_object(pk, request.user)
        serializer = TaskSerializers(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        task = self.get_object(pk, request.user)
        task.delete()
        return Response(status=204)

#---------------------------------------------------------
#Model Achievement
# Returns all achievements for a specific role owned by the authenticated user
class RoleAchievementView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        role = get_object_or_404(Role, pk=pk, owner=request.user)
        achievement = role.achievement.all()
        serializer = AchievementSerializers(achievement, many=True)
        return Response(serializer.data, status=200)

# Handles listing and creating achievements for the authenticated user
class AchievementListCreateView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        achievement = Achievement.objects.filter(role__owner=request.user)
        serializer = AchievementSerializers(achievement, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = AchievementSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
# Handles retrieving, updating, and deleting a single achievement owned by the authenticated user
class AchievementDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user): 
        achievement = get_object_or_404(Achievement, pk=pk)
        if achievement.role.owner != user:
            raise PermissionDenied(" You do not have permission to access this Achievement.")
        return achievement

    def get(self, request, pk):
        achievement = self.get_object(pk, request.user)
        serializer = AchievementSerializers(achievement)
        return Response(serializer.data, status=200)
#---------------------------------------------------------
class SignUpView(APIView):
    permission_classes = [AllowAny]
    # When we recieve a POST request with username, email, and password. Create a new user.
    def post(self, request):
        # Using .get will not error if there's no username
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        # Actually create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create an access and refresh token for the user and send this in a response
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )