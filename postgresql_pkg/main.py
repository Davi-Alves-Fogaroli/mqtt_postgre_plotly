from connect_db import connect_database, disconnect_database
from insert import insert
from create_table import create_table

def main():
    connection, cursor = connect_database()
    
    create_table(connection, cursor) 
    insert(connection, cursor)
    disconnect_database(connection, cursor)

if __name__ == "__main__":
    main()