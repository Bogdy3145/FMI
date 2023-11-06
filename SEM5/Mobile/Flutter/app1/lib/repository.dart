import 'sql/sql_helper.dart'; // Import your SQLHelper class
import 'service.dart'; // Import the Service model

class ServiceRepository {
  // Method to fetch all services from the database
  Future<List<Service>> getAllServices() async {
    final List<Map<String, dynamic>> serviceData = await SQLHelper.getServices();
    return serviceData.map((data) => Service(
      id: data['id'],
      name: data['name'],
      provider: data['provider'],
      location: data['location'],
      radius: data['radius'],
      phone: data['phone'],
      price: data['price'],
    )).toList();
  }

  // Method to add a new service to the database
  Future<int> addService(Service service) async {
    return SQLHelper.createItem(
      service.name,
      service.provider,
      service.location,
      service.radius,
      service.phone,
      service.price,
    );
  }

  // Method to update an existing service in the database
  Future<int> updateService(Service service) async {
    print('Updating Service: $service'); 
    return SQLHelper.updateService(
      service.id,
      service.name,
      service.provider,
      service.location,
      service.radius.toString(),
      service.phone,
      service.price.toString(),
    );
  }

  // Method to delete a service from the database
  Future<void> deleteService(int id) async {
    await SQLHelper.deleteService(id);
  }
}
