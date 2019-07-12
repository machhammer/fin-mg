import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentCard3Component } from './content-card3.component';

describe('ContentCard3Component', () => {
  let component: ContentCard3Component;
  let fixture: ComponentFixture<ContentCard3Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContentCard3Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentCard3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
