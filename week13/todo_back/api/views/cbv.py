from api.models import TaskList
from api.serializers import TaskListSerializer2, TasksSErializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class TaskLists(APIView):
    def get(self, request):
        tasklist = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskListDetail(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer2(tasklist)
        return Response(serializer.data)

    def put(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer2(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        tasklist = self.get_object(pk)
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TasksforTaskList(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        tasklist = self.get_object(pk)
        tasks = tasklist.task_set.all()
        serializer = TasksSErializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)