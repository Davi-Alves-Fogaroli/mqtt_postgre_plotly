import psycopg2
from config import postgres_config


def connect_database():
    #connect to the database
    connection = None
    
    try:
        params = postgres_config()
        print("Connecting to the postgresSQL database ...")
        connection = psycopg2.connect(**params)

        #cursos objecti will help to create any queries on the database and retrieve data
        cursor = connection.cursor()
        print("PostgresSQL data base version: ")
        cursor.execute("SELECT version()")
    
        database_version = cursor.fetchone()
        print(database_version)

        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print("ERROR IN CONNECTION: ", error)
    
    finally:
        if connection is not None:
            connection.close()
            print("Database connection terminated")
