import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UsernameComponent } from './components/username/username.component';
import { GetprojectComponent } from './components/getproject/getproject.component';
import { GetspecificprojectComponent } from './components/getspecificproject/getspecificproject.component';


const routes: Routes = [
  { path: 'login', component: UsernameComponent },
  { path: 'projects', component: GetprojectComponent },
  { path: 'specificpj', component: GetspecificprojectComponent }

];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
    
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
