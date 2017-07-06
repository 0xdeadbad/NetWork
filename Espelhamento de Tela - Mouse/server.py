from threading import Thread
from package_dealer import check_and_install
from classes import Th
from socket_helper import recvall, recv_msg
from tka import stream

if check_and_install('pickle', 'socket', 'pyautogui', 'PIL', 'sys', 'io', 'struct'):
	print('Todas as dependências foram instaladas! Abra o programa novamente!')
	exit()
else:
	import pickle
	import socket
	from PIL import ImageGrab, Image, ImageFile, ImageTk
	import sys
	import io
	import struct
	import pickle
	ImageFile.LOAD_TRUNCATED_IMAGES = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('172.16.102.9' , 22122)
s.bind(addr)
s.listen(1)

class main:
	
	def __init__(self):
		print('Wainting connection!')
		self.conn, self.addr = s.accept()
		flag = True
		print('Connected')
		self.stream_gui = stream(self.conn, self)
		self.stream_thread = Th(self.stream_gui.create_gui)
		self.recv_thread = Th(self.recv_loop)
		self.stream_thread.start()
		self.recv_thread.start()

	def update_image(self, im): 
		img = Image.open(io.BytesIO(im))
		frame_image = ImageTk.PhotoImage(img)
		self.stream_gui.my_label.config(image=frame_image)
		self.stream_gui.my_label.image = frame_image
		
	def recv_loop(self):
		while True:
			msg = recv_msg(self.conn, self)
				
		
if __name__ == '__main__':
	app = main()
