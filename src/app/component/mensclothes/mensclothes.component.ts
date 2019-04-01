import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-electronics',
  templateUrl: './mensclothes.component.html',
  styleUrls: ['./mensclothes.component.css']
})
export class MensclothesComponent implements OnInit {
  name:String;
  price:number;
  model:String;
  size:String;
  isEdit:boolean;
  isEdit2:boolean;
  isEdit3:boolean;
  constructor() { }

  ngOnInit() {
    
    this.name = "Avirex Fly Air Force flight jacket fur collar genuine leather jacket For men black";
    this.model = "Avirex Fly Air Force";
    this.price = 55000;
    this.size = "s,m,l";
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