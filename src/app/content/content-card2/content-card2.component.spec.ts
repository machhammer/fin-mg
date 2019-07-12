import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentCard2Component } from './content-card2.component';

describe('ContentCard2Component', () => {
  let component: ContentCard2Component;
  let fixture: ComponentFixture<ContentCard2Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContentCard2Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentCard2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
