import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs'
import {ReferenceService} from '../services/reference.service'
import {Index} from '../models/index'
import {Equity} from '../models/equity'

import { isThisTypeNode } from 'typescript';



@Component({
  selector: 'app-asset-finder',
  templateUrl: './asset-finder.component.html',
  styleUrls: ['./asset-finder.component.css']
})

export class AssetFinderComponent implements OnInit{

  private indices: Index[] = [];
  private equities: Equity[] = [];
  

  displayedColumns_indices: string[] = ['index', 'country'];
  displayedColumns_equities: string[] = ['index', 'country', 'company', 'symbol', 'sector'];

  constructor(private referenceService: ReferenceService) {
    
  }  

  ngOnInit() {
    this.referenceService.getIndices().subscribe((res: Index[]) => {
      this.indices = res
    })
    this.referenceService.getEquities().subscribe((res: Equity[]) => {
      this.equities = res
    })
  }
}
