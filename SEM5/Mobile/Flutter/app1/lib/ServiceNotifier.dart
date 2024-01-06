import 'package:flutter/material.dart';

import 'service.dart';

class ServiceNotifier extends ChangeNotifier {
  List<Service> _services = [];
  List<Service> get services => _services;
  

 void setServices(List<Service> services) {
    _services = services;
    notifyListeners();
  }
  void addService(Service service) {
    _services.add(service);
    notifyListeners();
  }

  void deleteService(int id) {
  
    _services.removeWhere((service) => service.id == id);
    
    notifyListeners();
     
  }

  void updateService(Service updatedService) {
  final index = _services.indexWhere((service) => service.id == updatedService.id);
  if (index != -1) {
    _services[index] = updatedService;
    notifyListeners();
  }
}


bool serviceExists(int id) {
  return services.any((service) => service.id == id);
}


   int findHighestId() {
    int highestId = 0;
    for (final service in _services) {
      if (service.id > highestId) {
        highestId = service.id;
      }
    }
    print("Found highest id is:$highestId");
    return highestId;
  }

  int findLowestId(){
    int lowestId = _services[0].getId();
    for (final service in _services) {
      if (service.id < lowestId) {
        lowestId = service.id;
      }
    }
    
    print("Found lowest id is:$lowestId");
    return lowestId;
  }

  
}
