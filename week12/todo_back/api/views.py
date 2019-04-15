import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import TaskList, Task
from django.views.decorators.csrf import csrf_exempt
from api.serializers import TaskSerializer, TaskSerializer2, ProductSerializer

def index(request):
    return HttpResponse('<h1>What is your main focus for today?</h1>')

@csrf_exempt
def tasklists(request):
    if request.method == 'GET':
        tasklist = TaskList.object.all()
        serializer = TaskSerializer2(tasklist, many=True)
        json_tasks = [serializer.data for a in tasklist]
        return JsonResponse(json_tasks, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskSerializer2(data= body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return  JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_detail(request, pk):
    try:
        tasklist = TaskList.object.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(tasklist.to_json())

    if request.method == 'GET':
        serializer = TaskSerializer(tasklist)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskSerializer(instance=tasklist,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        tasklist.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


def tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    tasks = tasklist.task_set.all()
    serializer = ProductSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)
