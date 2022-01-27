from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff', 'tasks']
class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']

class TaskSerializer(serializers.ModelSerializer):
    tasks = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Task
        fields = ['author', 'title', 'text', 'created_date', 'published_date', 'tasks']