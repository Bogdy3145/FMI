import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-username',
  templateUrl: './username.component.html',
  styleUrls: ['./username.component.css']
})

export class UsernameComponent {
  
  userName: string = '';

  saveName() {
    localStorage.setItem('userName', this.userName);
    console.log(localStorage.getItem('userName'));
  }
}