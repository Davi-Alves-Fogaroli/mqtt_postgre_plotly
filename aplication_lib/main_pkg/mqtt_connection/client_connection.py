from .callbacks import on_connect, on_subscribe, on_menssage
import paho.mqtt.client as mqtt

class MqttClientConnection:
    def __init__(self, broker_ip:  str, port: int, client_name: str, keepalive):
        self._broker_ip = broker_ip
        self._port = port 
        self._client_name = client_name
        self._keepalive = keepalive
        self._mqtt_client = None

    def start_connection(self):
        
        try:
            mqtt_client = mqtt.Client(self._client_name) #paho-mqtt==1.6.1 version
        except:
            mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)  #paho-mqtt==2.0 version (powerShell just work with this comand version)
        
        #callbacks
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_menssage

        #inicia conecção do cliente com o broker
        mqtt_client.connect(host=self._broker_ip, port=self._port, keepalive=self._keepalive)    
        self._mqtt_client = mqtt_client
        mqtt_client.loop_start()

    # def end_connection(self):
    #     try:
    #         self._mqtt_client.loop_stop()
    #         self._mqtt_client.disconnect()
    #         return True
    #     except:
    #         return False
