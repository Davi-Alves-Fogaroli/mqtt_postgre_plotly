# Psycopg3 suport asynchronous feature
import psycopg2
#put passwors in .env
 
#connect to the database
connection_object = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="123",
                        port="5432",
                        )

#cursos objecti will help to create any queries on the database and retrieve data
cursor = connection_object.cursor()

cursor.execute("CREATE TABLE sensor(engine_speed float, pressure float, fluid_level float ,temperature float)")

cursor.execute("INSERT INTO sensor(engine_speed, pressure, fluid_level, temperature) values (11,12,13,14)")

cursor.execute("SELECT * FROM sensor")

print(cursor.fetchall())

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