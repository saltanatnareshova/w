import { Injectable } from '@angular/core';
import { TasklistService } from './task-list.service';
import { HttpClient } from '@angular/common/http';
import { ITasklist, ITasks, IAuthResponse } from '../models/models';

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
  createTaskList(name: any): Promise<ITasklist> {
    return this.post('http://127.0.0.1:8000/api/tasklist/', {
    //tslint:disable-next-line: object-literal-shorthand
      name: name
    });
  }

  updateTaskList(tasklist: ITasklist): Promise<ITasklist> {
    return this.put(`http://127.0.0.1:8000/api/tasklist/${tasklist.id}/`, {
      name: tasklist.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/tasklist/${id}/`, {});
  }
  auth(login: any, password: any): Promise<IAuthResponse>{
    return this.post('http://127.0.0.1:8000/api/login/', {
      username: login,
      password: password
    });
  }
  logout(): Promise<any>{
    return this.post('http://127.0.0.1:8000/api/logout/', {

    });
  }
}