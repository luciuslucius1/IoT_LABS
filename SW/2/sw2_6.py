import paho.mqtt.client as PahoMQTT
import time

Broker_mqtt = "test.mosquitto.org"
Port_mqtt = 1883
Topic = "/Catalog"

class MyMQTTPublisher:
	def __init__(self, clientID, topic, broker, port):
		self.clientID = clientID
		self._paho_mqtt = PahoMQTT.Client(self.clientID, False) 
		self._paho_mqtt.on_connect = self.myOnConnect
		self.messageBroker = broker

	def start (self):
		self._paho_mqtt.connect(self.messageBroker, port_mqtt)
		self._paho_mqtt.loop_start()

	def stop (self):
		self._paho_mqtt.loop_stop()
		self._paho_mqtt.disconnect()

	def myPublish(self, topic, message):
		self._paho_mqtt.publish(topic, message, 2)
		print("Message sent")

	def myOnConnect (self, paho_mqtt, userdata, flags, rc):
		print ("Connected to %s with result code: %d" % (self.messageBroker, rc))

if __name__ == "__main__":
	print(f"Connessione al broker: {Broker_mqtt} alla porta: {Port_mqtt}")
	my_mqtt = MyMQTTPublisher("IoT device_publisher", Topic, Broker_mqtt, Port_mqtt)
	my_mqtt.start()

	done = False
	device1={
        "Device": "Dispositivo1", 
        "risorse": "tante", 
        "end_points":[0, 1, 2]
        }
	while True:
		my_mqtt.myPublish(Topic, str(device1))
		time.sleep(5)
