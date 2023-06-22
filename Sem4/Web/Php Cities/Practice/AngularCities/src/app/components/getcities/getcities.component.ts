import { Component } from '@angular/core';
import { City } from 'src/app/City';
import { CityService } from 'src/app/city.service';
import {Location} from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-getcities',
  templateUrl: './getcities.component.html',
  styleUrls: ['./getcities.component.css']
})
export class GetcitiesComponent {
  cities: City[] = [];
  selectedCity: City = { Id:0, Name: '', County: ''}; // Define the selectedBook property

  constructor(private cityService: CityService, private location: Location, private router: Router) {}

  ngOnInit() {
    this.getAllCities();
  }

  getAllCities(){
    this.cityService.getAllCities().subscribe(
      (data: any) => {
        this.cities = data;
        console.log(this.cities);
      }
    );
  }

  selectCity(city: City) {
    this.selectedCity = { ...city }; // Copy the selected book into the selectedBook property

    localStorage.setItem('localid',city.Id.toString());
    localStorage.setItem('names',JSON.stringify(city.Name.toString()));

    console.log(city.Id);

    this.router.navigate(['/city', city.Id]);
    
  }
}
