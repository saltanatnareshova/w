from django.db import models
import datetime


class TaskList(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return '{}:{}'.format(self.id, self.name)
    def to_json(self):
        return{
            'id':self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(datetime.datetime.now())
    due_on = models.DateTimeField(datetime.datetime.now())
    status = models.CharField(max_length=200)
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{};{}'.format(self.name,self.created_at,self.due_on, self.status)

    def to_json(self):
        return {
            'name':self.name,
            'created_at':self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'tasklist':self.tasklist
        }
