import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-content-card4',
  templateUrl: './content-card4.component.html',
  styleUrls: ['./content-card4.component.css']
})
export class ContentCard4Component implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  title = 'Browser market shares at a specific website, 2014';
   type = 'PieChart';
   data = [
      ['Firefox', 45.0],
      ['IE', 26.8],
      ['Chrome', 12.8],
      ['Safari', 8.5],
      ['Opera', 6.2],
      ['Others', 0.7] 
   ];
   columnNames = ['Browser', 'Percentage'];
   options = {          
   };
   //width = 100;
   //height = 100;
}
