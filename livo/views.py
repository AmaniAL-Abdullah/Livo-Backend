from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Role, Task, Achievement
from .serializers import RoleSerializers, TaskSerializers, AchievementSerializers


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