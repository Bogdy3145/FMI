class Service {
  int id;
  String name;
  String provider;
  String location;
  int radius;
  String phone;
  int price;

  Service({
    required this.id,
    required this.name,
    required this.provider,
    required this.location,
    required this.radius,
    required this.phone,
    required this.price,
  });

  Service copyWith({
    int? id,
    String? name,
    String? provider,
    String? location,
    int? radius,
    String? phone,
    int? price,
  }) {
    return Service(
      id: id ?? this.id,
      name: name ?? this.name,
      provider: provider ?? this.provider,
      location: location ?? this.location,
      radius: radius ?? this.radius,
      phone: phone ?? this.phone,
      price: price ?? this.price,
    );
  }

  @override
  String toString() {
    return 'Service(id: $id, name: $name, provider: $provider, location: $location, radius: $radius, phone: $phone, price: $price)';
  }
}
