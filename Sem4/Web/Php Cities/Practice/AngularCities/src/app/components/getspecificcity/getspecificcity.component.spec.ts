import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetspecificcityComponent } from './getspecificcity.component';

describe('GetspecificcityComponent', () => {
  let component: GetspecificcityComponent;
  let fixture: ComponentFixture<GetspecificcityComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GetspecificcityComponent]
    });
    fixture = TestBed.createComponent(GetspecificcityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
