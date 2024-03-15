try:
	import usocket as socket
except:
	import socket

import network
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Aloalo'
password = 'hel0.o812'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
	pass

print('CONECCTED SUCCESSFUL !!!')
print(station.ifconfig())
