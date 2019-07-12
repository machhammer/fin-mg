import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentCard5Component } from './content-card5.component';

describe('ContentCard5Component', () => {
  let component: ContentCard5Component;
  let fixture: ComponentFixture<ContentCard5Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContentCard5Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentCard5Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
