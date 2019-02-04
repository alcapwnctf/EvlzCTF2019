import requests
import os
import datetime
import time
import socket
import sys
import subprocess
import threading
import asyncio
from threading import Timer

THREADS=[]

class thread(threading.Thread):
	""" Extended Thread to allow handling SIGINT """
	def __init__(self):
		self.alive = True
		threading.Thread.__init__(self)


class RepeatedTimer(object):
	def __init__(self, interval, function, *args, **kwargs):
		self._timer     = None
		self.interval   = interval
		self.function   = function
		self.args       = args
		self.kwargs     = kwargs
		self.is_running = False
		self.start()

	def _run(self):
		self.is_running = False
		self.start()
		self.function(*self.args, **self.kwargs)

	def start(self):
		if not self.is_running:
			self._timer = Timer(self.interval, self._run)
			self._timer.start()
			self.is_running = True

	def stop(self):
		self._timer.cancel()
		self.is_running = False

class service():
	def __init__(self, name, port, serviceType, response, size, path, repair=True, toFile=True):
		
		self.name=name
		self.port=port
		self.serviceType=serviceType
		self.response=response
		self.path=path
		self.repair=repair
		self.toFile=toFile
		self.size=size
		self.badResponse="evlz{evlzBADRESPONSEctf}ctf"

		self.logTheMessage("Repair set to {}".format(self.repair))
		self.logTheMessage("Log to file set to {}".format(self.toFile))

	def logTheMessage(self, logMessage):
		logmessage=""
		logmessage+=str(datetime.datetime.now())
		logmessage+=" -> "+logMessage
		
		print (logmessage)
		
		if self.toFile:
			f=open('/home/toor/Desktop/logfile','a')
			f.write(logMessage)
			f.close()

	def checkweb(self):
		try:
			response=requests.get('http://127.0.0.1:{}'.format(self.port))
			response=response.text
		except:
			response=self.badResponse
		
		if self.response in response: return True
		else: return False

	def checktcp(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1.0)
		server_address = ('127.0.0.1', self.port)

		try:
			sock.connect(server_address)
			response=sock.recv(self.size)
			response=str(response)
			sock.close()

		except:
			response=self.badResponse
		
		if self.response in response: return True
		else: return False

	
	def check(self):

		if self.serviceType=='web' and self.checkweb():self.logTheMessage("{} running perfectly at port {}".format(self.name, self.port))

		elif self.serviceType=='tcp' and self.checktcp():self.logTheMessage("{} running perfectly at port {}".format(self.name, self.port))

		else: 
			self.logTheMessage("{} failed heath check at port {}".format(self.name, self.port))
			if self.repair:
				self.logTheMessage("Restarting {} at {}".format(self.name, self.path))
				result=subprocess.Popen(["docker-compose","-f",self.path+'docker-compose.yml',"down"],stdout=subprocess.PIPE)
				message,error=result.communicate()
				self.logTheMessage("docker-compose down returned: {}".format(message))

				result=subprocess.Popen(["docker-compose","-f",self.path+'docker-compose.yml',"up"],stdout=subprocess.PIPE)
				message,error=result.communicate()
				self.logTheMessage("docker-compose up returned: {}".format(message))

class serviceThread(thread):
	def __init__(self, name, port, serviceType, response, size, path, repair, toFile, interval, tillWhen, *args, **kwargs):
		thread.__init__(self)
		
		self.name=name
		self.port=port
		self.serviceType=serviceType
		self.response=response
		self.path=path
		self.repair=repair
		self.toFile=toFile
		self.interval=interval
		self.tillWhen=tillWhen
		self.size=size
		self.myService = service(self.name, self.port, self.serviceType, self.response, self.size, self.path, self.repair, self.toFile)

	def run(self):
		repeat=RepeatedTimer(self.interval, self.myService.check)
		try:
			if self.alive:time.sleep(self.tillWhen+30)
		finally:
			repeat.stop()

"""Services list"""

# thread=serviceThread("chall name",chall port,"chall type(web/tcp)","message that response should contain","size of data to recieve","path of dockerfile", bool val to repair the service, write log to file, poll interval, number of seconds this should run)
# THREADS.append(thread)

if __name__=='__main__':
	for thread in THREADS:
		thread.start()
	time.sleep(300)

	print("Finished with the checks")
	sys.exit(0)