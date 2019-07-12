import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentCard6Component } from './content-card6.component';

describe('ContentCard6Component', () => {
  let component: ContentCard6Component;
  let fixture: ComponentFixture<ContentCard6Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContentCard6Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentCard6Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
