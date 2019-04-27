from api.models import TaskList
from api.serializers import TaskListSerializer2, TasksSErializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

class TaskLists(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    http_method_names = ['get', 'post']

class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


