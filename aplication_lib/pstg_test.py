# Psycopg3 suport asynchronous feature
#put passwors in .env
import sys
import psycopg2
from boil_data_pkg import sensor_data_generator as sdg

# !!!create path connection to be able import boil_data_pkg!!!
# print("\n",18*'-', "before insert sys.path: ", sys.path)
# sys.path.append('C://Users/davi.alves/analytic_eye_tests/paho_postgre/aplication_lib/boil_data_pkg') !faill >.<!
# print("\n", 18*'=', "after insert sys.path: ", sys.path, "\n\n")


#connect to the database
connection_object = psycopg2.connect(
                        host="localhost",
                        database="boil_data",
                        port="5432",
                        user="postgres",
                        password="123",
                        )

print(10*"-", "connection:", connection_object)
#cursos objecti will help to create any queries on the database and retrieve data
cursor = connection_object.cursor()
# print(10*"-", "cursor: ", cursor)

cursor.execute("CREATE DATABASE sensor")
cursor.execute("CREATE TABLE sensors_datas(name text, pressure float, temperature float, speed float); ")
# cursor.execute("INSERT INTO sensor VELUES", ('n', 1, 3, 4))

sensor_data = sdg()
sd = sensor_data

for sd in sd:
    print("\nsd: ", sd, "\n")
    n = sd["Name "]
    p = sd["pressure"]
    t = sd["temperature"]
    s = sd["speed"]
    cursor.execute(f"INSERT INTO sensor(name, pressure, temperature, speed) VALUES ({n, p, t, s}) ;")

select = cursor.execute("SELECT * FROM sensor ;")

print(cursor.execute("SELECT * FROM sensor ;"))

# connection_object.commit() #exist on psycopg2 ? (this method saving changes)

# cursor.close()
# connection_object.close()

#.execute() -> submit query string
# cursor.execute("SELECT * FROM example_table")

#.fetchone() -> fetc[busca] data from your data base. returns first row before execute a query
# print(cursor.fetchone())

#.fechall() -> well, return all row of the data base
#print(cursor.fetchall())

#.fetchmany() -> you can expecify how many row you want see usin 'size=int' argument
#print(cursor.fechmany(size=5))