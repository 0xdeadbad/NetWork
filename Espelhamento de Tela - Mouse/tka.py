import tkinter as tk
from classes import Th
from PIL import Image, ImageTk, ImageGrab
from socket_helper import send_msg
from pickle import dumps

class stream:

	def __init__(self, socket, app):
		self.socket = socket
		self.app = app

	def create_gui(self):
		self.root = tk.Tk()
		self.my_label = tk.Label(self.root)
		self.my_label.bind('<Button-1>', self.screen_click)
		self.my_label.bind('<Motion>', self.screen_motion)
		self.disconnectButton = tk.Button(self.root, text='Desconectar', command=self.disconnect)
		self.my_label.grid()
		self.disconnectButton.grid(pady=5)
		self.root.mainloop()
		
	def disconnect(self):
		self.socket.close()
		
	def screen_click(self, event):
		
		send_msg(self.socket, dumps((event.x, event.y)), 1)
		
	def screen_motion(self, event):
		send_msg(self.socket, dumps((event.x, event.y)), 2)
		
#stream('s').create_gui()
