import { Component, OnInit } from '@angular/core';
import {ReferenceService} from '../../services/reference.service'
import {MatPaginator, MatTableDataSource, MatSort} from '@angular/material';

import {Equity} from '../../models/equity'


@Component({
  selector: 'app-tab-one',
  templateUrl: './tab-one.component.html',
  styleUrls: ['./tab-one.component.css']
})
export class TabOneComponent implements OnInit {

  displayedColumns: string[] = ['symbol', 'company', 'country', 'sector', 'performance'];

  private equities: Equity[] = [];

  equities_datasource = new MatTableDataSource<Equity>(this.equities);



  constructor(private referenceService: ReferenceService) { }

  ngOnInit() {

    this.referenceService.getLooser().subscribe((res: Equity[]) => {
      this.equities = res
      this.equities_datasource.data = this.equities;
    })
  }

  sortData(event) {
  }

}
