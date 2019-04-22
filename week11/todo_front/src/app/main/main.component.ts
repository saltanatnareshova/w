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
}
