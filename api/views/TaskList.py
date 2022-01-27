from django.conf import settings
from django.contrib.auth.models import User
import redis
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status, permissions, mixins, generics, renderers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from ..models import Task
from ..serializers import UserSerializer, TaskSerializer
from rest_framework import permissions

# redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
#                                   port=settings.REDIS_PORT, db=0)
# class TaskList(APIView):
#     def get(self, request, format=None):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        print(request.data.keys())
        key = list(request.data.keys())[0]
        value = request.data[key]
        # redis_instance.set(key, value)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TaskHighlight(generics.GenericAPIView):
    queryset = Task.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.highlighted)