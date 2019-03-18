import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-electronics',
  templateUrl: './electronics.component.html',
  styleUrls: ['./electronics.component.css']
})
export class ElectronicsComponent implements OnInit {
  name:String;
  price:number;
  model:String;
  color:String;
  isEdit:boolean;
  isEdit2:boolean;
  isEdit3:boolean;
  constructor() { }

  ngOnInit() {
    
    this.name = "Apple MacBook Pro 13 Intel Core i5 2300";
    this.model = "Apple";
    this.price = 650000;
    this.color = "silver black darkblue";
  }
  showEdit(){
    this.isEdit = !this.isEdit;
    this.isEdit2 = false;
    this.isEdit3 = false;
  }
  showEdit2(){
    this.isEdit2 = !this.isEdit2;
    this.isEdit = false;
    this.isEdit3 = false;
  }
  showEdit3(){
    this.isEdit3 = !this.isEdit3;
    this.isEdit = false;
    this.isEdit2 = false;
  }
}
