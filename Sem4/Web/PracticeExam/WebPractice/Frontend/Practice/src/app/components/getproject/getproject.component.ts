import { Component } from '@angular/core';
import { Project } from 'src/app/models/Project';
import { SoftwaredevService } from 'src/app/services/softwaredev.service';

@Component({
  selector: 'app-getproject',
  templateUrl: './getproject.component.html',
  styleUrls: ['./getproject.component.css']
})
export class GetprojectComponent {
  projects: Project[] = []

  constructor (private softwareDeveloperService: SoftwaredevService) {}


  getProjects(){
    this.softwareDeveloperService.
      getProjects().
      subscribe((result: Project[]) => (this.projects = result));
  }
}
