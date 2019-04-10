from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import TaskList, Task


def index(request):
    return HttpResponse('<h1>What is your main focus for today?</h1>')

def tasklists(request):
    tasklist = TaskList.object.all()
    json_tasks=[a.to_json() for a in tasklist]

    return JsonResponse(json_tasks, safe=False)

def task_detail(request, pk):
    try:
        tasklist = TaskList.object.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(tasklist.to_json())

def tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    tasks = tasklist.task_set.all()
    json_task = [a.to_json() for a in tasks]
    return JsonResponse(json_task, safe=False)
