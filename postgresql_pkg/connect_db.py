from config import postgres_config
import psycopg2 as db


def connect_database():
    #connect to the database
    connection = None
    
    try:
        params = postgres_config()
        print("Connecting to the postgresSQL database ...")
        connection = db.connect(**params)
        print(f"Autocommit: {connection.autocommit} and Isolation level: {connection.isolation_level}")

        #cursos objecti will help to create any queries on the database and retrieve data
        cursor = connection.cursor()
        print("PostgresSQL data base version: ")
        cursor.execute("SELECT version()")
    
        database_version = cursor.fetchone()
        print(database_version)

        # print(10*'=',"CONNECT: ", connection)
        # print(10*'=',"CURSOR: ", cursor)

    except(Exception, db.DatabaseError) as error:
        print("ERROR IN CONNECTION: ", error)

    return connection, cursor

def disconnect_database(connection, cursor):
    if connection is not None:
        connection.close()
        cursor.close()
        print(f"Database connection terminated") 
        # print(f"Connection status: {connection}")
        # print(f"Cursor status: {cursor}")
