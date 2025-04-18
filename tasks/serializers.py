from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'user', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
