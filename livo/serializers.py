from rest_framework import serializers
from .models import Role, Task, Achievement

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class AchievementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'