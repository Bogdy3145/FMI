export interface Link {
    Id: number;
    CityId1: number;
    CityId2: number;
    Distance: number;
    Duration: number;
    CityName1?: string; // Add CityName property
    CityName2?: string; // Add CityName property
}