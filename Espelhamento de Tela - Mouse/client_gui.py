import tkinter as tk
import errno, socket

class Application:
	
	def __init__(self, s):
		
		self.connected = False
		self.s = s
		
	def create_gui(self):
		self.root = tk.Tk()
		
		self.ipLabel = tk.Label(text='Digite o IP a se conectar: ')
		self.ipEntry = tk.Entry()
		
		self.portLabel = tk.Label(text='Digite a porta a ser utilizada: ')
		self.portEntry = tk.Entry()
		
		self.connectButton = tk.Button(text='Conectar', command=lambda: self.connect((self.ipEntry.get(), int(self.portEntry.get()))))
		
		self.ipLabel.grid()
		self.ipEntry.grid()
		
		self.portLabel.grid()
		self.portEntry.grid()
		
		self.connectButton.grid(pady=5)
		
		self.root.mainloop()
		
	def connect(self, addr):
		self.addr = addr
		print(self.addr)
		try:
			self.s.connect(self.addr)
			self.connected = True
			print('You are connected!')
		except socket.error as e:
			print('Something gone wrong!')
			self.connected = False
		if self.connected:
			self.update('connected')
			
	def disconnect(self):
		self.connected = False
		self.s.close()
		self.update('disconnected')
	
	def update(self, status):
		if status == 'connected':
			self.ipEntry.config(state='disabled')
			self.portEntry.config(state='disabled')
			self.connectButton.config(text='Disconnect', command=self.disconnect)
		elif status == 'disconnected':
			self.ipEntry.config(state='normal')
			self.portEntry.config(state='normal')
			self.connectButton.config(text='Connect')
			
