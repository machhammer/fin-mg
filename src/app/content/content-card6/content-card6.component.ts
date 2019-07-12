import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-content-card6',
  templateUrl: './content-card6.component.html',
  styleUrls: ['./content-card6.component.css']
})
export class ContentCard6Component implements OnInit {

  constructor() { }
  title = 'Company Hiring Report';  
  type = 'ComboChart';  
  data = [  
     ["Account", 3, 2, 2.5],  
     ["HR",2, 3, 2.5],  
     ["IT", 1, 5, 3],  
     ["Sales", 3, 9, 6],  
     ["Marketing", 4, 2, 3]  
  ];  
  columnNames = ['Loaction','India','US','Average'];  
  options = {     
     hAxis: {  
        title: 'Department'  
     },  
     vAxis:{  
        title: 'Employee hired'  
     },  
     seriesType: 'bars',  
     series: {2: {type: 'line'}}  
  };  
  width = 600;  
  height = 400;  
  
  ngOnInit() {  
  }  

}
