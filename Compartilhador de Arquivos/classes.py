import tkinter as tk
from tkinter.filedialog import askopenfilename as af
import socket
from socket_helper import *
from threading import Thread
from pickle import dumps, loads
from tkinter import ttk


def raw(text):
	new_string = ''
	for char in text:
		if char == '\\':
			new_string += '/'
		else:
			new_string += char
	return new_string

class Th(Thread):
	
	def __init__(self, func, args=()):
		
		Thread.__init__(self)
		self.func = func
		self.args = args
		
	def run(self):
		
		self.func(*self.args)

class Application:
	
	def __init__(self, title):
		
		self.items = {}
		
		self.root = tk.Tk()
		
		self.root.resizable(width=False, height=False)
		
		self.root.wm_title(title)
		
		self.files = {}
		
	def start(self):
		
		self.root.mainloop()
		
	def add_widget(self, item, name, args={}):
		
		if name not in self.items:
				
			self.items[len(self.items)] = [name , item(self.root, **args)]
			
	def get_widget(self, name):
		
		for k in self.items:
			
			if self.items[k][0] == name:
				
				return self.items[k][1]
				
		return None	
		
	def pack_all(self):
		
		for i in range(len(self.items)):
			
			self.items[i][1].grid(padx=2, pady=2)
			
class Socket_tcp:
	
	def __init__(self, app):
		
		self.app = app
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sh = socket_helper(app)
		
	class Client:
		
		def __init__(self, app):
			
			Socket_tcp.__init__(self, app)
			
		
		def connect(self, addr):
			
			self.s.connect(addr)
			
			Th(self.recv, (self.s, )).start()
		
		def recv(self, c):
		
			while True:
				
				msg = self.sh.recv_msg(c)
				
				if msg[1] == 0:
					
					if msg[0].decode() == 'break':
					
						break
						
				elif msg[1] == 1:
				
					items = loads(msg[0])
					
					for item in items:
						
						if item >= self.app.get_widget('filesBox').size():
							
							self.app.get_widget('filesBox').insert(item, items[item])
							
				elif msg[1] == 10:
					
					with open(self.app.get_widget('filesBox').get(msg[2]), 'wb') as f:
						
						f.write(msg[0])
			
		def send(self, c, msg, msgtype, adic=999):
			
			self.sh.send_msg(c, msg, msgtype, adic)
			
		def request_file(self, index):
			
			self.send(self.s, b'file_request', 5, index)
			
		
	class Server:
	
		def __init__(self, app, addr=('localhost', 22122), backlog=5):
			
			Socket_tcp.__init__(self, app)
			self.s.bind(addr)
			self.s.listen(backlog)
			self.clients = {}
		
		def file_send(self, file_path, c, index):
		
			with open(file_path, 'rb') as f:
						
				fd = f.read()
				self.send(c, fd, 10, adic=index)
		
		def recv(self, c):
		
			while True:
				
				msg = self.sh.recv_msg(c)
				
				if msg[1] == 0:
					
					if msg[0].decode() == 'break':
					
						break
						
				if msg[1] == 5:
					
					file_path = raw(self.app.files[msg[2]])
					print('Requested: ', file_path)
					
					Th(self.file_send, (file_path, c, msg[2])).start()
			
		def send(self, c, msg, msgtype, adic=999):
			
			self.sh.send_msg(c, msg, msgtype, adic)
			
		def listen(self):
		
			while True:
				
				print('Listening')
				
				client = self.s.accept()
				
				
				print('Got connection')
				
				cid = len(self.clients)
				self.clients[cid] = (client[0], Th(self.recv, (client[0],)))
				self.clients[cid][1].start()
				
				self.send_update(client[0])
				
		def send_update(self, c=None):
			
			list_items = {}
			for i in range(self.app.get_widget('filesBox').size()):
				list_items[i] = self.app.get_widget('filesBox').get(i)
			
			if c:
				self.send(c, dumps(list_items), 1)
			else:
				for client in self.clients:
					self.send(self.clients[client][0], dumps(list_items), 1)
