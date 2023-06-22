import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, filter } from 'rxjs';
import { City } from 'src/app/City';
import {Link} from 'src/app/models/Link';

@Injectable({
    providedIn: 'root'
  })
  export class CityService {
  
    private API: string = 'http://localhost/Practice/AngularCities/PHP';
    constructor(private http: HttpClient) { }

    getAllCities(){
        const url = `${this.API}/GetCities.php`;
        return this.http.get<City[]>(url);
    }

    getAllLinks(){
        const url = `${this.API}/GetLinks.php`;
        return this.http.get<Link[]>(url);
    }

    getSpecificLinks(id: number){

        const params = new HttpParams().set('id', id.toString());
        
        
        const url = `${this.API}/GetSpecificLinks.php`;
        const options = { params: params };

        console.log(url);
      
        return this.http.get<City[]>(url, options);
    }

    
      
    
}