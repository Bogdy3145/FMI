import { Component } from '@angular/core';
import { SoftwareDeveloper } from './models/SoftwareDeveloper';
import { SoftwaredevService } from './services/softwaredev.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  // title = 'Practice';
  // developers: SoftwareDeveloper[] = [];

  // constructor (private softwareDeveloperService: SoftwaredevService) {}

  // ngOnInit() : void {
  //   this.softwareDeveloperService.
  //   getSoftwareDevelopers().
  //   subscribe((result: SoftwareDeveloper[]) => (this.developers = result));
    
  //   console.log(this.developers);
  //}
}
