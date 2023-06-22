import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GetcitiesComponent } from './components/getcities/getcities.component';
import {Location} from '@angular/common';
import { GetspecificcityComponent } from './components/getspecificcity/getspecificcity.component';

const routes: Routes = [
  {path: 'cities', component: GetcitiesComponent},
  { path: 'city/:id', component: GetspecificcityComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
