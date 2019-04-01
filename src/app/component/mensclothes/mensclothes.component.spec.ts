import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MensclothesComponent } from './mensclothes.component';

describe('MensclothesComponent', () => {
  let component: MensclothesComponent;
  let fixture: ComponentFixture<MensclothesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MensclothesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MensclothesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});