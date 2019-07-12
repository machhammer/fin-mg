import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentCard1Component } from './content-card1.component';

describe('ContentCard1Component', () => {
  let component: ContentCard1Component;
  let fixture: ComponentFixture<ContentCard1Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContentCard1Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentCard1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
