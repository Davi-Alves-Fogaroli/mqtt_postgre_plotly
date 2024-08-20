import psycopg2 as db

def create_table(connection, cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS boil_data(
                    Name VARCHAR(255) NOT NULL,
                    pressure FLOAT NOT NULL,
                    temperature FLOAT NOT NULL,
                    speed FLOAT NOT NULL
                    );""")
    
    connection.commit()

    return
