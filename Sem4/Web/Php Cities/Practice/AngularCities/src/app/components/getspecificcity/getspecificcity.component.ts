import { Component } from '@angular/core';
import { City } from 'src/app/City';
import { CityService } from 'src/app/city.service';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';
import {Location} from '@angular/common';
import { Link } from 'src/app/models/Link';


@Component({
  selector: 'app-getspecificcity',
  templateUrl: './getspecificcity.component.html',
  styleUrls: ['./getspecificcity.component.css']
})
export class GetspecificcityComponent {
  cities: City[] = [];
  selectedCity: City = { Id:0, Name: '', County: ''}; // Define the selectedBook property
  filteredCities: City[] =[];


  links: Link[] = [];
  filteredLinks: Link[] = [];

  constructor(private cityService: CityService, private location: Location, private router: Router) {}

  ngOnInit() {
    this.getLinkedCities();
    //console.log(this.filteredCities)
  }

  getLinkedCities() {
    
    const idToFilter = localStorage.getItem('localid');
    //console.log(idToFilter);
    
  
    if (idToFilter) {
      this.cityService.getSpecificLinks(parseInt(idToFilter)).subscribe(
        (data: City[]) => {
          // Handle the data returned from the HTTP request

          //console.log(data);
          // Update the filteredLinks property or perform any other necessary actions
          this.filteredCities = data;
        }
      );
    }
  


    // const idToFilter = localStorage.getItem('localid');

    // console.log(idToFilter);

    // if (idToFilter){
    //   this.cityService.getAllLinks().subscribe((data: Link[]) => {
    //     this.links = data;
    //     this.filteredLinks = this.links.filter(link => {console.log('CityId1:', link.CityId1);
    //     console.log('CityId2:', link.CityId2);
    //     console.log('idToFilter:', +idToFilter);
    //     return ((link.CityId1 === +idToFilter) || (link.CityId2 === +idToFilter));});
        
    //   });
    // console.log(this.filteredLinks);
    
  //}
    
  }

  selectCity(city: City) {
    //this.selectedCity = { ...city }; // Copy the selected book into the selectedBook property

    localStorage.setItem('localid',city.Id.toString());
    localStorage.setItem('name', city.Name.toString());
    

    const localname = localStorage.getItem('names');
    if (localname){
    var before = JSON.parse(localname);
    var full = before + " " + city.Name;
    full = JSON.stringify(full);
    localStorage.setItem('names',full);

    console.log(localStorage.getItem('names'));
    }

    //console.log(localStorage.getItem('names'));


    //console.log(city.Id);
    
    this.router.navigate(['/city', city.Id]);

    this.getLinkedCities();
    
    

   
    //this.location.go('/city/' + city.id);

  }

  selectLink(link: Link){
    //console.log(link.Id);
    
    this.router.navigate(['/city', link.Id]);
  }

}
