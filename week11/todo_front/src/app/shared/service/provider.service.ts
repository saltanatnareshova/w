import { Injectable } from '@angular/core';
import { TasklistService } from './task-list.service';
import { HttpClient } from '@angular/common/http';
import { ITasklist, ITasks } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends TasklistService{

  constructor(http:HttpClient){
    super(http);  
  }

  getTaskList():Promise<ITasklist[]>{
     return this.get('http://127.0.0.1:8000/api/tasklist/', {});
  }

  getTasks(tasklist: ITasklist): Promise<ITasks[]> {
    return this.get(`http://127.0.0.1:8000/api/tasklist/${tasklist.id}/tasks`, {});
  }
}