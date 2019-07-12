import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-content-card5',
  templateUrl: './content-card5.component.html',
  styleUrls: ['./content-card5.component.css']
})
export class ContentCard5Component implements OnInit {

  constructor() { }

  title = 'Company Hiring Report';  
  type = 'GeoChart';  
  data = [  
     ['Country', 'Popularity'],
     ['Germany', 200],
     ['United States', 300],
     ['Brazil', 400],
     ['Canada', 500],
     ['France', 600],
     ['RU', 700]
  ];  
    
  width = 600;  
  height = 400;   

  ngOnInit() {
  }

}
