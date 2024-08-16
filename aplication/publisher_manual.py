import paho.mqtt.client as mqtt
from data_generation import sensor_data_generator

#sensor_data[
#   {"Name ": data, "pressure": data, "temperature": data, "speed": data},
#   {"Name ": data, "pressure": data, "temperature": data, "speed": data},
#   ]
sensor_data = sensor_data_generator()

for x in range(len(sensor_data)):
    mqtt_client = mqtt.Client("Publishe "+sensor_data[0]["Name "])
    mqtt_client.connect(host="localhost", port=1883)
    mqtt_client.publish(topic="/sensor_data", payload=f'{sensor_data[x]}')

mqtt_client = mqtt.Client("meu_publisher")
mqtt_client.connect(host="localhost", port=1883)
mqtt_client.publish(topic="/mensages", payload='{"minha": "mensagem"}')
