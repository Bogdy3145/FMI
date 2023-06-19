import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
//import { EditDevComponent } from './components/edit-dev/edit-dev.component';
import { FormsModule } from '@angular/forms';
import { UsernameComponent } from './components/username/username.component';
import { GetprojectComponent } from './components/getproject/getproject.component';
import { GetspecificprojectComponent } from './components/getspecificproject/getspecificproject.component';

@NgModule({
  declarations: [
    AppComponent,
    
    UsernameComponent,
         GetprojectComponent,
         GetspecificprojectComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
