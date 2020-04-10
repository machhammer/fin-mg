import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { DomSanitizer } from '@angular/platform-browser';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  /** Based on the screen size, switch from standard to one column per row */
  cards = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        return [
          { title: 'Looser', cols: 2, rows: 1, content: 'hallo1'},
          { title: 'Winner', cols: 2, rows: 1, content: '' },
          { title: 'Card 3', cols: 2, rows: 1, content: 'hallo3' },
          { title: 'Card 4', cols: 2, rows: 1, content: 'hallo4' }
        ];
      }

      return [
        { title: 'Looser', cols: 1, rows: 1, content: 'hallo5' },
        { title: 'Winner', cols: 1, rows: 1, content: 'hallo6' },
        { title: 'Card 3', cols: 1, rows: 1, content: 'hallo7' },
        { title: 'Card 4', cols: 1, rows: 1, content: 'hallo8' }
      ];
    })
  );

  constructor(private breakpointObserver: BreakpointObserver, private sanitizer: DomSanitizer) {}

}
