import 'package:flutter/material.dart';
import 'repository.dart';
import 'service.dart';
import 'service_detail.dart';
import 'service_add.dart';

void main() {
  runApp(MaterialApp(
    home: MainPage(),
  ));
}

class MainPage extends StatefulWidget {
  @override
  _MainPageState createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  final ServiceRepository _serviceRepository = ServiceRepository();
  List<Service> _services = [];

  @override
  void initState() {
    super.initState();
    _loadServices();
  }

  void _loadServices() async {
    final services = await _serviceRepository.getAllServices();
    setState(() {
      _services = services;
    });
  }

 void _addService() async {
  // Navigate to the page for adding a new service and receive the result
  final newServiceAdded = await Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => ServiceAddPage(),
    ),
  );

  if (newServiceAdded == true) {
    // Reload services if a new service was added successfully
    _loadServices();
  }
}



  void _deleteService(int id) async {
  // Show a confirmation dialog
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("Confirm Deletion"),
        content: Text("Are you sure you want to delete this service?"),
        actions: <Widget>[
          TextButton(
            child: Text("Cancel"),
            onPressed: () {
              // Close the dialog
              Navigator.of(context).pop();
            },
          ),
          TextButton(
            child: Text("Delete"),
            onPressed: () async {
              // Delete the service and reload services
              await _serviceRepository.deleteService(id);
              _loadServices();

              // Close the dialog
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}


  void _updateService(Service service) async {
    final result = await _serviceRepository.updateService(service);
    print('Service updated ssssuccessfully');

    if (result > 0) {
      _loadServices();
      print('Service updated ssssuccessfully');
    } else {
      print('Failed to update service');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Service List'),
      ),
      body: ListView.builder(
        itemCount: _services.length,
        itemBuilder: (context, index) {
          final service = _services[index];
          return ListTile(
            title: Text(service.name),
            subtitle: Text(service.provider),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => ServiceDetailPage(
                    service: service,
                    onUpdate: (updatedService) {
                      _updateService(updatedService);
                    },
                    onDelete: _deleteService,
                  ),
                ),
              );
            },

            trailing: IconButton(
              icon: Icon(Icons.delete),
              onPressed: () {
                _deleteService(service.id);
              },
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _addService,
        child: Icon(Icons.add),
      ),
    );
  }
}
