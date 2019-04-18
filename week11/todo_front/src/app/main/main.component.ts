import { Component, OnInit } from '@angular/core';
import { ITasklist, ITasks } from '../shared/models/models';
import { ProviderService } from '../shared/service/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public tasklists: ITasklist[]= [];
  public tasks: ITasks[] = [];

  constructor(private provider:ProviderService) { }


  ngOnInit() {
    this.provider.getTaskList().then(res=>{
      console.log(res);

      this.tasklists = res;
    });
  }
}
