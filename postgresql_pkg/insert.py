import sys
sys.path.append("/Users/davi.alves/analytic_eye_tests/paho_postgre")
sys.path.append("/Users/davi.alves/analytic_eye_tests/paho_postgre/aplication_lib")

from aplication_lib.boil_data_pkg.data_generator import sensor_data_generator as sdg
import psycopg2 as db

#sensor_data[
#   {"Name ": data, "pressure": data, "temperature": data, "speed": data},
#   ]

def insert(connection, cursor):
# print(10*'-',"connection: ", connection)
# print(10*'-',"cursor: ", cursor)
    sensor_data = sdg()

    for sd in sensor_data:
        # print("\nsd: ", sd, "\n")
        n = sd["Name "]
        p = sd["pressure"]
        t = sd["temperature"]
        s = sd["speed"]

        cursor.execute("""INSERT INTO boil_data (name, pressure, temperature, speed) 
                       VALUES (%s,%s,%s,%s);""",
                       (n,p,t,s))
        
        connection.commit()
    
    # cursor.execute("DELETE FROM boil_data;")
    # print(100*'=', cursor.fetchall())
    # cursor.execute("SELECT * FROM boil_data;")
    # print(100*'=', cursor.fetchall())
    # cursor.execute("SELECT * FROM boil_data WHERE pressure = '4.0';")
    # print(100*'=', cursor.fetchall())


# connection_object.commit() #exist on psycopg2 ? (this method saving changes)

# cursor.close()
# connection_object.close()

#.execute() -> submit query string
# cursor.execute("SELECT * FROM example_table")

#.fetchone() -> fetc[busca] data from your data base. returns first row before execute a query
# print(cursor.fetchone())

#.fetchall() -> well, return all row of the data base
#print(cursor.fetchall())

#.fetchmany() -> you can expecify how many row you want see usin 'size=int' argument
#print(cursor.fechmany(size=5))