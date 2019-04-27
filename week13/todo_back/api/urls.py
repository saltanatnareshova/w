from django.urls import path
from api import views
#urlpatterns = [
#   path('', old_w12.index),
#    path('tasklist/', fbv.tasklists),
#    path('tasklist/<int:pk>/', fbv.task_detail),
#    path('tasklist/<int:pk>/tasks', fbv.tasks),
#]

urlpatterns = [
    #path('', views.old_w12.index),
    path('tasklist/', views.TaskLists.as_view()),
    path('tasklist/<int:pk>/', views.TaskListDetail.as_view()),
    #path('tasklist/<int:pk>/tasks', views.TasksforTaskList.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)
]