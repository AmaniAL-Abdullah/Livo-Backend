from rest_framework import serializers
from .models import Role, Task, Achievement

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'owner']
        read_only_fields = ['id', 'owner'] 

    def create(self, validated_data):
        user = self.context['request'].user 
        return Role.objects.create(owner=user, **validated_data)


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'start_date', 'end_date', 'role']
        read_only_fields = ['id', 'start_date'] 

class AchievementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'title', 'description', 'date', 'role']
        read_only_fields = ['id', 'date'] 
