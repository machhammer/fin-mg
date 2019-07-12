import { Component, OnInit, AfterContentInit } from '@angular/core';
import { Router } from '@angular/router';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-content-layout',
  templateUrl: './content-layout.component.html',
  styleUrls: ['./content-layout.component.css']
})
export class ContentLayoutComponent implements OnInit, AfterContentInit {

  constructor(private router: Router, private readonly route: ActivatedRoute) {
    console.log(route.parent.url)
  }

  ngOnInit() {
    this.router.navigate(['content', { outlets: { out1: ['card1'], out2: ['card2'], 
                                                  out3: ['card3'], out4: ['card4'], 
                                                  out5: ['card5'], out6: ['card6'] 
                                                } }]);
    //this.router.navigate(['content', { outlets: { out2: ['card2'] } }]);
    //this.router.navigate(['content', { outlets: { out3: ['card3'] } }]);
    //this.router.navigate(['content', { outlets: { out4: ['card4'] } }]);
  
    
  }

  ngAfterContentInit() {
  
  }

}
