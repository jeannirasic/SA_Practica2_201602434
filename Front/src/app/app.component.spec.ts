import { TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';

describe('AppComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [
        AppComponent
      ],
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should validate variable respuesta`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.respuesta).toEqual('');
  });

  it(`should change variable respuesta`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    fixture.nativeElement.querySelector('button').click();
    fixture.detectChanges();
    const app = fixture.componentInstance;
    expect(app.respuesta).toEqual('correcto');
  });

  it('should validate title', () => {
    const fixture = TestBed.createComponent(AppComponent);
    expect(fixture.nativeElement.querySelector('h2').textContent).toEqual('Contactame');
  });
});