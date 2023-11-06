import 'package:flutter/material.dart';
import 'repository.dart'; // Import your ServiceRepository
import 'service.dart'; // Import the Service model

class ServiceAddPage extends StatefulWidget {
  @override
  _ServiceAddPageState createState() => _ServiceAddPageState();
}

class _ServiceAddPageState extends State<ServiceAddPage> {
  final ServiceRepository _serviceRepository = ServiceRepository();

  // Create a Service object to store the form data
  Service _newService = Service(
    id: 0,
    name: '',
    provider: '',
    location: '',
    radius: 0,
    phone: '',
    price: 0,
  );

  final _formKey = GlobalKey<FormState>();

  void _saveService() async {
  if (_formKey.currentState!.validate()) {
    // Save the new service to the database
    final newServiceId = await _serviceRepository.addService(_newService);

    if (newServiceId > 0) {
      // Service was added successfully
      print('Service added successfully');
      Navigator.pop(context, true); // Return 'true' to indicate success
    } else {
      // Failed to add service
      print('Failed to add service');
      Navigator.pop(context, false); // Return 'false' to indicate failure
    }
  }
}


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Service'),
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: EdgeInsets.all(16.0),
          children: <Widget>[
            TextFormField(
              decoration: InputDecoration(labelText: 'Name'),
              onChanged: (value) {
                setState(() {
                  _newService.name = value!;
                });
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a name';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Provider'),
              onChanged: (value) {
                _newService.provider = value!;
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a provider';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Location'),
              onChanged: (value) {
                _newService.location = value!;
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a location';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Radius'),
              onChanged: (value) {
                _newService.radius = int.parse(value!);
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a radius';
                }
                return null;
              },
              keyboardType: TextInputType.number,
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Phone'),
              onChanged: (value) {
                _newService.phone = value!;
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a phone number';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Price'),
              onChanged: (value) {
                _newService.price = int.parse(value!);
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a price';
                }
                return null;
              },
              keyboardType: TextInputType.number,
            ),
            ElevatedButton(

              onPressed: _saveService,
              child: Text('Submit'),
            ),
          ],
        ),
      ),
    );
  }
}
