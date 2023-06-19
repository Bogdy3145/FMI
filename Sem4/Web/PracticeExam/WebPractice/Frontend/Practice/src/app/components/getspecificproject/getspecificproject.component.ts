import { Component } from '@angular/core';
import { Project } from 'src/app/models/Project';
import { SoftwaredevService } from 'src/app/services/softwaredev.service';

@Component({
  selector: 'app-getspecificproject',
  templateUrl: './getspecificproject.component.html',
  styleUrls: ['./getspecificproject.component.css']
})
export class GetspecificprojectComponent {
  projects: Project[] = []

  constructor (private softwareDeveloperService: SoftwaredevService) {}
  
  getProjects() {
    const userName = localStorage.getItem('userName'); // Get the user's name from localStorage
  
    if (userName !== null) {
      this.softwareDeveloperService.getProjects()
        .subscribe((result: Project[]) => {
          this.projects = result.filter(pj => {
            const projectMembers = pj.members.split(',').map(member => member.trim()); // Split and trim the members string
            return projectMembers.includes(userName);
          });
        });
    }
  }
  
  
  ngOnInit() {
    this.getProjects();
  }
  
  
}
