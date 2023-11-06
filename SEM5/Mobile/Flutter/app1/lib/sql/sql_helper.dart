import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart' as sql;

class SQLHelper{
  static Future<void> createTables(sql.Database database) async {
    await database.execute("""CREATE TABLE services(
      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      name TEXT,
      provider TEXT,
      location TEXT,
      radius INTEGER,
      phone TEXT,
      price INTEGER
    )""");
    print('Table "services" created successfully');
  }

  static Future<sql.Database> db() async {
    return sql.openDatabase(
      'bogdan.db',
      version: 1,
      onCreate: (sql.Database database, int version) async{
        await createTables(database);
      }
    ); 
  }

  static Future<int> createItem(String name, String provider, String location, int radius, String phone, int price) async {
      final db = await SQLHelper.db();

      final data = {'name':name, 'provider': provider, 'location': location, 'radius': radius, 'phone': phone, 'price': price};
      final id = await db.insert('services', data, conflictAlgorithm: sql.ConflictAlgorithm.replace);

      return id;

  }

  static Future<List<Map<String, dynamic>>> getServices() async{
    final db = await SQLHelper.db();
    return db.query('services', orderBy: "id");
  }

  static Future<List<Map<String, dynamic>>> getItem(int id) async {
    final db = await SQLHelper.db();
    return db.query('services', where: "id = ?", whereArgs: [id], limit: 1);
  }

  static Future<int> updateService(
    int id, String name, String provider, String location, String radius, String phone, String price) async{
        final db = await SQLHelper.db();

        final data = {
          'name': name,
          'provider': provider,
          'location': location,
          'radius': radius,
          'phone': phone,
          'price': price
        };
        final result =
        await db.update('services', data, where: "id = ?", whereArgs: [id]);
        print('DATABASE Service: $data');
        return result;
    }
  
  static Future<void> deleteService(int id) async{
    final db = await SQLHelper.db();
    try{
      await db.delete("services", where: "id = ?", whereArgs: [id]);
    }
    catch (err){
      debugPrint("Something went wrong with deleting the service: $err");
    }
  }
    
  
}
