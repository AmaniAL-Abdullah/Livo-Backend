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

# Create your views here.
class RoleListCreateView(APIView):

    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializers(role, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = RoleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

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