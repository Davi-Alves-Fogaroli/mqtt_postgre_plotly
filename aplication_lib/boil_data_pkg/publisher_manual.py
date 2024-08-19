import paho.mqtt.client as mqtt
from boil_data_pkg.data_generaton import sensor_data_generator
import time 

#sensor_data[
#   {"Name ": data, "pressure": data, "temperature": data, "speed": data},
#   {"Name ": data, "pressure": data, "temperature": data, "speed": data},
#   ]

sensor_data = sensor_data_generator()
# print(sensor_data)
for x in range(len(sensor_data)):
    # print(sensor_data, "x ", x)
    mqtt_client = mqtt.Client("Publishe "+sensor_data[0]["Name "])
    mqtt_client.connect(host="localhost", port=1883)
    mqtt_client.publish(topic="/sensor_data", payload=f'{sensor_data[x]}')
    time.sleep(2)

# for some reason need import time if we want to publish 2 diferent payload usin for structure before another publish
    # import time 
    # # time.sleep(2)
    # mqtt_client = mqtt.Client("meu_publisher")
    # mqtt_client.connect(host="localhost", port=1883)
    # mqtt_client.publish(topic="/sensor_data", payload="{'minha: mensagem'}")
