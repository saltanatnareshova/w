from django.urls import path
from api import views

urlpatterns = [
    path('', views.index),
    path('tasklist/', views.tasklists),
    path('tasklist/<int:pk>/', views.task_detail),
    path('tasklist/<int:pk>/tasks', views.tasks),
]