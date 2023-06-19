import { Injectable } from '@angular/core';
import { SoftwareDeveloper } from '../models/SoftwareDeveloper';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Project } from '../models/Project';

@Injectable({
  providedIn: 'root'
})
export class SoftwaredevService {

private url = "SoftwareDeveloper";

  constructor(private http: HttpClient) { }

  public getSoftwareDevelopers() : Observable<SoftwareDeveloper[]> {
    return this.http.get<SoftwareDeveloper[]>('https://localhost:7061/api/SoftwareDeveloper');
  }

  public getProjects() : Observable<Project[]> {
    return this.http.get<Project[]>('https://localhost:7061/api/Project');
  }
}
