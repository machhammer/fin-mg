import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentCard4Component } from './content-card4.component';

describe('ContentCard4Component', () => {
  let component: ContentCard4Component;
  let fixture: ComponentFixture<ContentCard4Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContentCard4Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentCard4Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
