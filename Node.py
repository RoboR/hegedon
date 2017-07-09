import paho.mqtt.client as mqtt
import threading


class NodeClass:
    mqttClient = None
    topic = None
    messageCB = None

    
    def run(self, server, port, keepalive):
        t = threading.Thread(target=self.__connect, args=(server, port, keepalive))
        t.start()


    def __connect(self, server, port, keepalive):
        self.mqttClient.connect(server, port, keepalive)
        self.mqttClient.loop_forever()


    # The callback for when the client receives a CONNACK response from the server.
    def __on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.mqttClient.subscribe(self.topic)


    # The callback for when a PUBLISH message is received from the server.
    def __on_message(self, client, userdata, msg):
        #print'{} {}'.format(msg.topic, str(msg.payload) )
        self.messageCB(msg)


    def __init__(self, topic, command=lambda: messageCB()):
        self.mqttClient = mqtt.Client() 
        self.topic = topic
        self.mqttClient.on_connect = self.__on_connect
        self.mqttClient.on_message = self.__on_message
        self.messageCB = command
