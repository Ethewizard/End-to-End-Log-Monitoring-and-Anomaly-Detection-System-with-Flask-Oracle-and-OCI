import cx_Oracle

DB_USER = 'admin'
DB_PASSWORD = 'your_password'
DB_DSN = 'your_db_high'  # Use the TNS alias or a direct connection string

def connect():
    try:
        connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, DB_DSN)
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"❌ Error connecting to Oracle: {e}")
        return None

def create_table():
    connection = connect()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                CREATE TABLE logs (
                    id NUMBER GENERATED ALWAYS AS IDENTITY,
                    log_message VARCHAR2(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            connection.commit()
            print("✅ Table created")
        except cx_Oracle.DatabaseError as e:
            print(f"❌ Error creating table: {e}")
        finally:
            cursor.close()
            connection.close()

def insert_log(log_message):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO logs (log_message) VALUES (:1)', [log_message])
            connection.commit()
        except cx_Oracle.DatabaseError as e:
            print(f"❌ Error inserting log: {e}")
        finally:
            cursor.close()
            connection.close()

def query_logs():
    connection = connect()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT * FROM logs')
            rows = cursor.fetchall()
            return rows
        except cx_Oracle.DatabaseError as e:
            print(f"❌ Error querying logs: {e}")
        finally:
            cursor.close()
            connection.close()
