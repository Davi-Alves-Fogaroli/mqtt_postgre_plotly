import random

data = ["Name ", "pressure", "temperature", "speed"]

def sensor_data_generator():
    sensor_data = [] 

    for x in range(2):
        dictionary = {}

        pressure = random.randint(0, 20)
        temperature = random.randint(0, 20)
        speed = random.randint(0, 20)

        dictionary = {data[0] : "Sensor "+str(x+1)}
        dictionary[data[1]] = pressure
        dictionary[data[2]] = temperature
        dictionary[data[3]] = speed

        sensor_data.append(dictionary)

    return sensor_data

# print(sensor_data)