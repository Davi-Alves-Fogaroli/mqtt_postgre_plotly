# Psycopg3 suport asynchronous feature
#put passwors in .env
import psycopg2
from data_generation import sensor_data_generator as sdg

#connect to the database
connection_object = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="123",
                        port="5432",
                        )

#cursos objecti will help to create any queries on the database and retrieve data
cursor = connection_object.cursor()

cursor.execute("CREATE TABLE sensor(name text, pressure float, temperature float, speed float)")
cursor.execute("INSERT INTO sensor(name, pressure, temperature, speed) values ('n', 1, 3, 4)")
# sensor_data = sdg()
# sd = sensor_data
# print
# for sd in sd:
#     n = sd["Name "]
#     p = sd["pressure"]
#     t = sd["temperature"]
#     s = sd["speed"]
#     cursor.execute(f"INSERT INTO sensor(name, pressure, temperature, speed) values ({n, p, t, s})")

# select = cursor.execute("SELECT * FROM sensor")

print(cursor.execute("SELECT * FROM sensor"))

cursor.close()
connection_object.close()

#.execute() -> submit query string
# cursor.execute("SELECT * FROM example_table")

#.fetchone() -> fetc[busca] data from your data base. returns first row before execute a query
# print(cursor.fetchone())

#.fechall() -> well, return all row of the data base
#print(cursor.fetchall())

#.fetchmany() -> you can expecify how many row you want see usin 'size=int' argument
#print(cursor.fechmany(size=5))