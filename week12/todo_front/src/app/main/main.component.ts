import { Component, OnInit } from '@angular/core';
import { ITasklist, ITasks } from '../shared/models/models';
import { ProviderService } from '../shared/service/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public tasklist: ITasklist[]= [];
  public tasks: ITasks[] = [];
  public name: any = '';

  constructor(private provider:ProviderService) { }


  ngOnInit() {
    this.provider.getTaskList().then(res=>{
      console.log(res);

      this.tasklist = res;
    });
  }
  getTasks(tasklist: ITasklist){
    this.provider.getTasks(tasklist).then(res => {
      console.log(res);

      this.tasks = res;
    })  
  }

  updateTaskList(task:ITasklist){
    this.provider.updateTaskList(task).then(res => {
      console.log(task.name + 'updated');
    })
  }

  deleteTaskList(task:ITasklist){
    this.provider.deleteTaskList(task.id).then(res =>{
      console.log(task.name + 'deleted');
      this.provider.getTaskList().then(r =>{
        this.tasklist = r;
      });
    });
  }

  createTaskList(){
    if(this.name != ''){
      this.provider.createTaskList(this.name).then(res =>{
        this.name = '';
        this.tasklist.push(res);
      });
    }
  }
}
