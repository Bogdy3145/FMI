import 'package:flutter/material.dart';
import 'repository.dart';
import 'service.dart';

class ServiceDetailPage extends StatefulWidget {
  final Service service;
  final Function(Service) onUpdate; // Add this line
  final void Function(int) onDelete; // Add this line
  
ServiceDetailPage({
    required this.service,
    required this.onUpdate,
    required this.onDelete,
  });
  @override
  _ServiceDetailPageState createState() => _ServiceDetailPageState();
}

class _ServiceDetailPageState extends State<ServiceDetailPage> {
  final _formKey = GlobalKey<FormState>();
  late Service _editedService;

  @override
  void initState() {
    super.initState();
    _editedService = widget.service;
  }

  void  _saveChanges() async {
    if (_formKey.currentState!.validate()) {
      final updatedService = Service(
        id: _editedService.id,
        name: _editedService.name,
        provider: _editedService.provider,
        location: _editedService.location,
        radius: int.parse(_editedService.radius.toString()),
        phone: _editedService.phone,
        price: int.parse(_editedService.price.toString()),
      );

      print('Updating Service: $updatedService');

      final result = await ServiceRepository().updateService(updatedService);

      if (result > 0) {
        print('Service updated successfully');
      } else {
        print('Failed to update service');
      }

      Navigator.pop(context);
    }
  }

  void _deleteService() async {
    await ServiceRepository().deleteService(_editedService.id);
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Service Details'),
        actions: <Widget>[
          IconButton(
          icon: Icon(Icons.save),
          onPressed: () {
            _saveChanges();
            widget.onUpdate(_editedService); // Call onUpdate with the updated service
          },
          ),

          IconButton(
            icon: Icon(Icons.delete),
            onPressed: () {
              _deleteService; // Pass the id as a parameter
  },
          ),
        ],
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: EdgeInsets.all(16.0),
          children: <Widget>[
            TextFormField(
              initialValue: _editedService.name,
              decoration: InputDecoration(labelText: 'Name'),
              onChanged: (value) {
                setState(() {
                  _editedService = _editedService.copyWith(name: value);
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
              initialValue: _editedService.provider,
              decoration: InputDecoration(labelText: 'Provider'),
              onChanged: (value) {
                setState(() {
                  _editedService = _editedService.copyWith(provider: value);
                });
              },
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter a provider';
                }
                return null;
              },
            ),
            TextFormField(
              initialValue: _editedService.location,
              decoration: InputDecoration(labelText: 'Location'),
              onChanged: (value) {
                setState(() {
                  _editedService = _editedService.copyWith(location: value);
                });
              },
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter a location';
                }
                return null;
              },
            ),
            TextFormField(
              initialValue: _editedService.radius.toString(),
              decoration: InputDecoration(labelText: 'Radius'),
              onChanged: (value) {
                setState(() {
                  _editedService = _editedService.copyWith(radius: int.parse(value));
                });
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
              initialValue: _editedService.phone,
              decoration: InputDecoration(labelText: 'Phone'),
              onChanged: (value) {
                setState(() {
                  _editedService = _editedService.copyWith(phone: value);
                });
              },
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter a phone number';
                }
                return null;
              },
            ),
            TextFormField(
              initialValue: _editedService.price.toString(),
              decoration: InputDecoration(labelText: 'Price'),
              onChanged: (value) {
                setState(() {
                  _editedService = _editedService.copyWith(price: int.parse(value));
                });
              },
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter a price';
                }
                return null;
              },
              keyboardType: TextInputType.number,
            ),
          ],
        ),
      ),
    );
  }
}
