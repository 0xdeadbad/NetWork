import socket
from threading import Thread

def int_input(msg):
	
	while True:
		
		try:
			
			x = int(input(msg))
			return x
			
		except ValueError:
			
			print('Digite um valor válido!')	

class Th(Thread):
	
	def __init__(self, func, args=()):
		
		Thread.__init__(self)
		self.func = func 
		self.args = args
		
	def run(self):
		
		self.func(*self.args)



def recv(s):

	msg, addr = s.recvfrom(1024)
	
	if msg.decode() == 'ping':
		
		Th(recv, (s,)).start()
		
		s.sendto(b'pong', addr)
		
		print('Ping from: ', addr)
		
if __name__ == '__main__':

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
	
		try:
			
			s.bind((input('Digite seu IP: '), int_input('Digite a porta a ser usada: ')))
			break
			
		except:
			print('Não foi possível formar o socket!')
			
	Th(recv, (s,)).start()
	
