import socket
from time import time
from random import randint

def int_input(msg, default=0):
	
	while True:
		
		try:
			
			x = int(input(msg))
			return x
			
		except ValueError:
			
			if not x:
				
				return 0
				
			else: 
				
				print('Digite um valor válido!')		

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	
	try:
		
		s.bind((input('Digite seu IP: '), randint(1024, 2**16-1)))
		timeout = int_input('Digite o timeout: ', default=5)
		s.settimeout(timeout)
		
		break
		
	except:
		
		print('Não foi possível formar o socket!')

addr = (input('Digite o IP de quem receberá o ping: '), int_input('Digite a porta de quem receberá o ping: '))



first = time()

s.sendto(b'ping', addr)

try:
	
	msg, addr = s.recvfrom(1024)

	if msg.decode() == 'pong':
			
		last = time()
			
		print(last - first)
	
except socket.timeout:
	
	print('Nada recebido, timeout!')
	
while True:
	
	pass
