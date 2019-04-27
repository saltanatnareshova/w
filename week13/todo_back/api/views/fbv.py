from api.models import TaskList
from api.serializers import TaskListSerializer2, TasksSErializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def tasklists(request):
    if request.method=='GET':
        tasklist = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE',])
def task_detail(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskListSerializer2(tasklist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer2(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', ])
def tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tasks = tasklist.task_set.all()
    serializer = TasksSErializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)