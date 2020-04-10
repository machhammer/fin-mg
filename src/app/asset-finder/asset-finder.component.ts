import {Component, OnInit, ViewChild} from '@angular/core';
import {ReferenceService} from '../services/reference.service'
import {Index} from '../models/index'
import {Equity} from '../models/equity'
import {MatPaginator, MatTableDataSource, MatSort} from '@angular/material';
import {animate, state, style, transition, trigger} from '@angular/animations';
import { CDK_CONNECTED_OVERLAY_SCROLL_STRATEGY } from '@angular/cdk/overlay/typings/overlay-directives';



@Component({
  selector: 'app-asset-finder',
  templateUrl: './asset-finder.component.html',
  styleUrls: ['./asset-finder.component.css'],
  animations: [
    trigger('detailExpand', [
      state('expanded', style({height: '*'})),
      state('collapsed', style({height: '0px', minHeight: '0', display: 'none'})),
      
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})

export class AssetFinderComponent implements OnInit{

  private indices: Index[] = [];
  private indices_copy: Index[] = [];
  private equities: Equity[] = [];
  private equities_copy: Equity[] = [];
  
  expandedElement: Equity;

  indices_datasource = new MatTableDataSource<Index>(this.indices);
  equities_datasource = new MatTableDataSource<Index>(this.equities);

  @ViewChild('indices_paginator', { static: false }) index_paginator: MatPaginator;
  @ViewChild('equity_paginator', { static: false }) equity_paginator: MatPaginator;
  @ViewChild('index_sort', {static: false}) index_sort: MatSort;
  @ViewChild('equity_sort', {static: false}) equity_sort: MatSort;

  searchValue = ""

  tabChanged_value = 0

  displayedColumns_indices: string[] = ['index', 'country'];
  displayedColumns_equities: string[] = ['index', 'country', 'symbol', 'company',  'sector', 'current_price', 'performance'];

  constructor(private referenceService: ReferenceService) {
    
  }  

  ngOnInit() {
    this.referenceService.getIndices().subscribe((res: Index[]) => {
      this.indices = res
      this.indices_copy = this.indices
      this.indices_datasource.data = this.indices;  
    
    })
    
    this.referenceService.getEquities().subscribe((res: Equity[]) => {
      this.equities = res
      this.equities_copy = res
      this.equities_datasource.data = this.equities;

    })
    
  }

  ngAfterViewInit() {
    this.indices_datasource.paginator = this.index_paginator;
    this.equities_datasource.paginator = this.equity_paginator;
    this.indices_datasource.sort = this.index_sort;
    this.equities_datasource.sort = this.equity_sort;
  }

  onSearch(event) {
   this.equities_datasource.filter = event.target.value.trim().toLowerCase();
   this.indices_datasource.filter = event.target.value.trim().toLowerCase();
  }

  tabChanged(event) {
    console.log("tab changed")
    this.equities_datasource.filter = "";
  }

}
