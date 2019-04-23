import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskListSerializer2, TasksSErializer


def index(request):
    return HttpResponse('<h1>What is your main focus for today?</h1>')

@csrf_exempt
def tasklists(request):
    if request.method=='GET':
        tasklist = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklist, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def task_detail(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    if request.method=='GET':
        serializer = TaskListSerializer(tasklist)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=tasklist, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method=='DELETE':
        tasklist.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})

def tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    tasks = tasklist.task_set.all()
    serializer = TasksSErializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)
