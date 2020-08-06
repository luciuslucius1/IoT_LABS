import paho.mqtt.client as mqtt
import time
import requests
import json


class MySubscriber:

	def __init__(self, clientID, serviceId, description):
		self.clientID = clientID
		# create an instance of paho.mqtt.client
		self._paho_mqtt = mqtt.Client(clientID, False) 

		# register the callback
		self._paho_mqtt.on_connect = self.myOnConnect
		self._paho_mqtt.on_message = self.myOnMessageReceived

		self.serviceId = serviceId
		self.descrizione = description
		self.end_points = []
		self.topic = 'null'
		self.messageBroker = 'null'
		self.port = -1


	def start (self):
		#manage connection to broker
		self._paho_mqtt.connect(self.messageBroker, 1883)
		self._paho_mqtt.loop_start()
		# subscribe for a topic
		if type(self.topic)==str:
			self._paho_mqtt.subscribe(self.topic, 2)
		else:	
			for t in self.topic:
				self._paho_mqtt.subscribe(t, 2)

	def stop (self):
		self._paho_mqtt.unsubscribe(self.topic)
		self._paho_mqtt.loop_stop()
		self._paho_mqtt.disconnect()

	def myOnConnect (self, paho_mqtt, userdata, flags, rc):
		print ("Connected to %s with result code: %d" % (self.messageBroker, rc))

	def myOnMessageReceived (self, paho_mqtt , userdata, msg):
		# A new message is received
		print ("Topic:'" + msg.topic+"', QoS: '"+str(msg.qos)+"' Message: '"+str(msg.payload) + "'")
	
	def registerOnCatalog(self):
		service = {
			"Servizi": self.serviceId,
			"descrizione": self.descrizione,
			"end_points": self.end_points
		}
		requests.put("http://localhost:8080/services/add", json = service)

	def getBrokerInfo(self):
		r = requests.get("http://localhost:8080/broker/info")
		info = json.loads(r.content.decode('utf-8'))
		self.messageBroker = info["brokerIp"]
		self.port = info["brokerPort"]
		
	
	def getDeviceTopic(self, deviceId):
		r = requests.get("http://localhost:8080/devices/search/"+deviceId)
		info = json.loads(r.content.decode('utf-8'))
		self.topic = info["end_points"]
		




if __name__ == "__main__":
	mysub = MySubscriber("MySubscriber 1", "S01", "MQTT subscriber che riceve messaggi sui valori di temperatura.")
	mysub.getDeviceTopic("ArduinoYun")
	mysub.registerOnCatalog()
	mysub.getBrokerInfo()
	mysub.start()
	while True:
		pass
	mysub.stop()
