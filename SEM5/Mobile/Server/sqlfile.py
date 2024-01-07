import sqlite3

DATABASE = 'bogdan.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db_connection()
    conn.execute("""CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        provider TEXT,
        location TEXT,
        radius INTEGER,
        phone TEXT,
        price INTEGER
    )""")
    conn.commit()
    conn.close()
    print('Table "services" created successfully')

def create_service(name, provider, location, radius, phone, price):
    conn = get_db_connection()
    sql = ''' INSERT INTO services(name, provider, location, radius, phone, price)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (name, provider, location, radius, phone, price))
    conn.commit()
    conn.close()

def get_services():
    conn = get_db_connection()
    services = conn.execute('SELECT * FROM services').fetchall()
    conn.close()
    return services

def update_service(id, name, provider, location, radius, phone, price):
    conn = get_db_connection()
    sql = ''' UPDATE services
              SET name = ?,
                  provider = ?,
                  location = ?,
                  radius = ?,
                  phone = ?,
                  price = ?
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (name, provider, location, radius, phone, price, id))
    conn.commit()
    conn.close()

def delete_service(id):
    conn = get_db_connection()
    sql = 'DELETE FROM services WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    conn.close()
