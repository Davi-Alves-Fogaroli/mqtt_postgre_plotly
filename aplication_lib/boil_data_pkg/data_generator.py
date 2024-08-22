import random
import datetime as dt
import pytz
import time
from file_dir_manipulated import create_file

time_zone = pytz.timezone("America/Sao_Paulo")
data = ["name ", "pressure", "temperature", "speed", "time"]

def sensor_data_generator():
    sensor_data = [] 

    for x in range(100):
        dictionary = {}
        time.sleep(random.uniform(0, 1))

        pressure = random.randint(0, 20)
        temperature = random.randint(0, 20)
        speed = random.randint(0, 20)
        current_time = dt.datetime.now(time_zone)

        dictionary = {data[0] : "Sensor "+str(x+1)}
        dictionary[data[1]] = pressure
        dictionary[data[2]] = temperature
        dictionary[data[3]] = speed
        dictionary[data[4]] = str(current_time.time())

        sensor_data.append(dictionary)

    return sensor_data

call = sensor_data_generator()
create_file(call)

print(call)
#sensor_data[
#   {"Name ": data, "pressure": data, "temperature": data, "speed": data},
#   {"Name ": data, "pressure": data, "temperature": data, "speed": data},
#   ]

# print(sensor_data)