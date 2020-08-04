import cherrypy
import json
import time
from sw2_1_Catalog import *

if __name__=='__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tool.session.on': True
		}
	}
	cherrypy.config.update({'server.socket_host':'localhost','server.socket_port': 8080})
	cherrypy.tree.mount(Broker(), '/broker', conf)
	cherrypy.tree.mount(Users(), '/users', conf)
	cherrypy.tree.mount(Services(), '/services', conf)
	cherrypy.tree.mount(Devices(), '/devices', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
