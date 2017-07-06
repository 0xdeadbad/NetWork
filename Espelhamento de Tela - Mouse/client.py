from package_dealer import check_and_install
from classes import Th
from socket_helper import send_msg, recv_msg
from client_gui import Application

if check_and_install('pickle', 'socket', 'pyautogui', 'PIL', 'sys', 'io'):
	print('Todas as dependências foram instaladas! Abra o programa novamente!')
	exit()
else:
	import socket
	from PIL import Image
	from pyautogui import screenshot as ImageGrab
	import io
	import pickle
	import pyautogui
	import random



class main:
	
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.gui = Application(self.s)
		Th(self.gui.create_gui).start()
		self.image_thread = Th(self.send_image)
		self.recv_thread = Th(self.recv_loop)
		while not self.gui.connected:
			pass
		self.image_thread.start()
		self.recv_thread.start()

	def recv_loop(self):
		
		while self.gui.connected:
			
			msg = recv_msg(self.s, self)
			
			
	
	def update_mouse(self, coords, t):
		if t == 1:
			print('Mouse updated: ', coords)
			pyautogui.click((coords[0]*2, coords[1]*2))
		elif t == 2:
			pyautogui.moveTo((coords[0]*2, coords[1]*2))

	def send_image(self):
		while self.gui.connected:
			imgBytes = io.BytesIO()
			im = ImageGrab() #bbox specifies specific region (bbox= x,y,width,height)
			img = im.resize((int(im.size[0]/2),int(im.size[1]/2)),Image.ANTIALIAS)
			img.save(imgBytes, format='JPEG', quality=85, optmize=True)
			send_msg(self.s, imgBytes.getvalue(), 0)
			#print('sent')
		
if __name__ == '__main__':
	app = main()
