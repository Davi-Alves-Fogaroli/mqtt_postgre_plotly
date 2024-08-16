from configs.broker_configs import mqtt_broker_configs

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"\nClient: {client} conectado com sucesso!!!")
        client.subscribe(mqtt_broker_configs["TOPIC_2"])
    else:
        print(f"Erro ao conectar, codigo rc: {rc}")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"\nCliente esta inscrito no topico: {mqtt_broker_configs["TOPIC_2"]}")
    print(f"QOS: {granted_qos}")

def on_menssage(client, userdata, message):
    print(f"\nMensagem recebida \n Cliente {client} \n Mensage {message}")
    print(f"Mensagem string {message.payload}")